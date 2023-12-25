from django.shortcuts import render, redirect
from .forms import ImageForm, IdCardForm
from .models import *
import pytesseract 
from PIL import Image
from django.conf import settings
import re
from pytesseract import Output
from datetime import datetime

# Create your views here.

def home(request):
    # Fetch all ID cards from the database
    all_id = ID_CARD.objects.all()
    context = {"all_id" : all_id}
    return render(request, 'home.html', context)

def scan_id(request):
    # Display form for uploading ID card image
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image and redirect to submit page
            image_instance = form.save()
            return redirect('submit_id/' + str(image_instance.id))
            
    context = {"form" : form}
    return render(request, 'scan-id.html', context)

def submit_id(request, image_id):
    # Extract text from the uploaded image using Tesseract OCR
    image_instance = ID_Image.objects.get(id=image_id)
    path = str(settings.MEDIA_ROOT)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pathz = path + "/" + str(image_instance.id_img)
    text = pytesseract.image_to_string(Image.open(pathz))
    d = pytesseract.image_to_data(pathz, output_type=Output.DICT)
    ocr_result = ocr(d)  # Extracted information from OCR

    # Create a form with extracted data for user verification
    model_instance = ID_CARD(**ocr_result)
    id_form = IdCardForm(instance=model_instance)

    if request.method == 'POST':
        id_form = IdCardForm(request.POST)
        if id_form.is_valid():
            # Save verified ID card information to the database
            ID_CARD.objects.create(
                identification_number=id_form.data['identification_number'],
                name=id_form.data['name'],
                last_name=id_form.data['last_name'],
                date_of_birth=id_form.data['date_of_birth'],
                date_of_issue=id_form.data['date_of_issue'],
                date_of_expiry=id_form.data['date_of_expiry'],
                id_card_img=image_instance
            )
            return redirect('/')
        else:
            print("error")

    context = {"id_form": id_form, "image_instance": image_instance}
    return render(request, 'verify-id.html', context)

def display_id(request, pk):
    # Display details of a specific ID card
    id_card = ID_CARD.objects.get(id=pk)
    context = {"id_card": id_card}
    return render(request, 'id_card.html', context)

def update_id(request, pk):
    # Update ID card information
    id_card = ID_CARD.objects.get(id=pk)
    id_form = IdCardForm(instance=id_card)

    if request.method == 'POST':
        id_form = IdCardForm(request.POST)
        if id_form.is_valid():
            # Save the updated information to the database
            id_card.identification_number = id_form.data['identification_number']
            id_card.name = id_form.data['name']
            id_card.last_name = request.POST.get("last_name")
            id_card.date_of_birth = request.POST.get("date_of_birth")
            id_card.date_of_issue = request.POST.get("date_of_issue")
            id_card.date_of_expiry = request.POST.get("date_of_expiry")
            id_card.save()
            return redirect('/id_card/' + pk)

    context = {'id_form': id_form, "image_instance": id_card.id_card_img}
    return render(request, 'verify-id.html', context)

def delete_id(request, pk):
    # Delete a specific ID card
    id_card = ID_CARD.objects.get(id=pk)
    id_card.delete()
    return redirect('/')

def ocr(d):
    # Extract relevant information from OCR results
    name_pattern = re.compile(r'(Mr|Mrs|Ms|Miss)\s[A-Za-z]+')
    date_pattern = re.compile(r'\d{2} [A-Za-z]{3}\. \d{4}')
    identification_pattern = re.compile(r'\d \d{4} \d{5} \d{2} \d')
    text_string = ' '.join(d['text'])
    
    # Extracting name, identification number, and dates
    name = name_pattern.search(text_string).group()
    identification_number = identification_pattern.search(text_string).group()
    dates = date_pattern.findall(text_string)

    try:
        # Try to find the "Lastname" keyword in the OCR results
        index = d['text'].index("Lastname")
        last_name = d['text'][index + 1]
    except ValueError:
        last_name = ""

    date_of_birth_string = dates[0] if len(dates) else ""
    date_of_issue_string = dates[1] if len(dates) > 1 else ""
    date_of_expiry_string = dates[2] if len(dates) > 2 else ""

    # Convert date strings to datetime objects
    date_of_birth = datetime.strptime(date_of_birth_string, "%d %b. %Y").date() if date_of_birth_string else None
    date_of_issue = datetime.strptime(date_of_issue_string, "%d %b. %Y").date() if date_of_issue_string else None
    date_of_expiry = datetime.strptime(date_of_expiry_string, "%d %b. %Y").date() if date_of_expiry_string else None

    result = {
        "name": name,
        "identification_number": identification_number,
        "date_of_birth": date_of_birth,
        "date_of_issue": date_of_issue,
        "date_of_expiry": date_of_expiry,
        "last_name": last_name
    }
    return result
