# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # Add new fields here
    # bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea)
    profile_picture = forms.ImageField(required=False)
    # date_of_birth = forms.DateField(required=False)
    # location = forms.CharField(max_length=255, required=False)
    # website = forms.URLField(required=False)
    # phone_number = forms.CharField(max_length=20, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'profile_picture')
