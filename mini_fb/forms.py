# File: forms.py
# Author: Raquel Gonzalez raquelgr@bu.edu
# Description: file to define the forms and their fields

from django import forms
from .models import Profile, StatusMessage

# Define a form for creating a new Profile
class CreateProfileForm(forms.ModelForm):
    # Form to create a new Profile.

    # Meta class to specify model and fields for the form
    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'city', 'email', 'image_url']

# Define a form for creating a new StatusMessage
class CreateStatusMessageForm(forms.ModelForm):
    #Form to create a new StatusMessage
    class Meta:
        model = StatusMessage
        fields = ['message']