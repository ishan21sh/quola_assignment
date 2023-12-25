# Thai ID Card OCR Project

This Django project allows users to upload images of Thai ID cards, perform OCR (Optical Character Recognition) on the images, and extract important information such as identification number, name, last name, date of birth, date of issue, and date of expiry. Users can verify and edit the detected values before saving the ID card information to the database. The project provides functionality to update or delete stored ID card information.

## Features

- Image upload for Thai ID cards
- OCR extraction of information (identification number, name, last name, date of birth, date of issue, date of expiry)
- Form to verify and edit detected values
- Database storage for ID card information
- Update and delete functionality for stored ID card information

## Project Setup

Follow the steps below to set up and run the project:

### Prerequisites

Make sure you have the following installed:

- Python (3.6 or higher)
- Django (3.0 or higher)

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/thai-id-ocr-project.git
cd thai-id-ocr-project
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- For Windows:

```bash
venv\Scripts\activate
```

- For Linux/macOS:

```bash
source venv/bin/activate
```

4. Install project dependencies:

```bash
pip install -r requirements.txt
```

### Database Setup

1. Apply migrations to create the database:

```bash
python manage.py migrate
```

### Running the Project

1. Start the development server:

```bash
python manage.py runserver
```


### Usage

1. Upload an image of a Thai ID card on the home page.
2. Verify and edit the detected values in the displayed form.
3. Save the ID card information to the database.
4. Use the update and delete functionalities as needed.

## Contribution

Feel free to contribute to the project by opening issues or creating pull requests. Your feedback and suggestions are highly appreciated.
