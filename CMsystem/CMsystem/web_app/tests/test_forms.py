from django.test import TestCase
from django.contrib.auth.models import User
from CMsystem.forms import UserRegisterForm, UserProfileform, ProfileUpdateForm, UserProfileUpdateform, statusupdate, ComplaintForm

class UserRegisterFormTest(TestCase):
    def test_valid_user_registration(self):
        form_data = {
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'newuser@example.com',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_user_registration_duplicate_email(self):
        # Create a user with the same email as in the form data
        User.objects.create_user(username='existinguser', email='existinguser@example.com', password='password123')

        form_data = {
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'existinguser@example.com',  # This email already exists
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('This email address is already in use.', form.errors['email'])