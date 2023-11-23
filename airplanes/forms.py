from django import forms
from django.core.exceptions import ValidationError
from PIL import Image 

class UploadFileForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32)
    files = forms.ImageField()

    def clean_files(self):
        uploaded_file = self.cleaned_data['files']
        try:
            # Attempt to open the uploaded image file using PIL
            Image.open(uploaded_file)
        except (IOError, ValueError) as e:
            # If opening the file fails or it's not a valid image, raise validation error
            raise ValidationError("The uploaded file is not a valid image.")
        return uploaded_file