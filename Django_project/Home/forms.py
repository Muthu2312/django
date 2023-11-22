# your_app/forms.py

from django import forms

class ImageUploadForm(forms.Form):
    original_image = forms.ImageField(label='Select an image for processing')
