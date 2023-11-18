from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from django.shortcuts import render, redirect
from .models import Profile,Complaint
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import requests

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    # add this to mark email mandatory
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        
    def clean_email(self):
            # Get the email
        username = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.exclude(pk=self.instance.pk).get(username=username)
            
            
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return username

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')
         