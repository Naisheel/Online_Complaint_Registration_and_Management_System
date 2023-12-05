from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from django.shortcuts import render, redirect
from .models import Profile,Complaint
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import requests
from django.contrib.auth.forms import PasswordChangeForm
from django.core.validators import MaxLengthValidator

class CustomPasswordChangeForm(PasswordChangeForm):

    def clean_new_password2(self):
        old_password = self.cleaned_data.get('old_password')
        new_password2 = self.cleaned_data.get('new_password2')

        if old_password and new_password2 and old_password == new_password2:
            raise forms.ValidationError("New password must be different from the old password.")

        return new_password2

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    # add this to mark email mandatory
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        help_texts = {
            'username': 'Required characters between 6 to 15  Letters, digits and @/./+/-/_ only',
        }
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
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        # Check if the input contains any numeric characters
        if any(char.isdigit() for char in first_name):
            raise forms.ValidationError("Numeric characters are not allowed in the first name.")

        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        # Check if the input contains any numeric characters
        if any(char.isdigit() for char in last_name):
            raise forms.ValidationError("Numeric characters are not allowed in the first name.")

        return last_name
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 6 or len(username) > 15:
            raise forms.ValidationError("Username must be between 6 and 15 characters.")

        return username


class UserProfileform(forms.ModelForm):
    class Meta:
        model=Profile 
        fields=('contact_number','Branch')
    


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    # first_name=forms.CharField( max_length=30, required=True)
    # last_name=forms.CharField( max_length=30, required=True)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
    help_texts = {
            'username': 'Required characters between 6 to 15  Letters, digits and @/./+/-/_ only',
        }
    
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
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        # Check if the input contains any numeric characters
        if any(char.isdigit() for char in first_name):
            raise forms.ValidationError("Numeric characters are not allowed in the first name.")

        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        # Check if the input contains any numeric characters
        if any(char.isdigit() for char in last_name):
            raise forms.ValidationError("Numeric characters are not allowed in the first name.")

        return last_name
    
class UserProfileUpdateform(forms.ModelForm):
    
    # collegename =forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    Branch=forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model=Profile
        fields=('contact_number','Branch','profile_pic')

class statusupdate(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=('status',)  
        help_texts = {
            'status': None,
          
        }    

class ComplaintForm(forms.ModelForm):
    Subject = forms.CharField(max_length=200, validators=[MaxLengthValidator(200)])
    Description = forms.CharField(
        max_length=500,
        validators=[MaxLengthValidator(500)],
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40})  # Adjust rows and cols as needed
    )

    class Meta:
        model=Complaint
        fields=('Subject','Type_of_complaint','Description')

