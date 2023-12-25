from django.forms import ModelForm,widgets
from django import forms
from .models import ID_Image,ID_CARD

class ImageForm(ModelForm):
    class Meta:
        model = ID_Image
        fields = '__all__'

class IdCardForm(ModelForm):
    class Meta:
        model = ID_CARD
        fields = '__all__'
        exclude = ['id_card_img']
        widgets = {
            'date_of_birth': widgets.DateInput(attrs={'type': 'date'}),
            'date_of_issue': widgets.DateInput(attrs={'type': 'date'}),
            'date_of_expiry': widgets.DateInput(attrs={'type': 'date'}),
        }