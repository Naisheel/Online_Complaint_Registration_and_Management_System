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

class UserProfileformTest(TestCase):
    def test_valid_user_profile_form(self):
        form_data = {
            'contact_number': '1234567890',
            'Branch': 'ICT',
        }
        form = UserProfileform(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_user_profile_form_empty_contact_number(self):
        form_data = {
            'contact_number': '',  # Empty contact number
            'Branch': 'ICT',
        }
        form = UserProfileform(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('This field is required.', form.errors['contact_number'])

class ProfileUpdateFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='existinguser', email='existinguser@example.com', password='password123')

    def test_valid_profile_update_form(self):
        form_data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'first_name': 'Updated',
            'last_name': 'User',
        }
        form = ProfileUpdateForm(instance=self.user, data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_profile_update_form_duplicate_email(self):
        form_data = {
            'username': 'existinguser',
            'email': 'existinguser@example.com',  # This email already exists
            'first_name': 'Updated',
            'last_name': 'User',
        }
        form = ProfileUpdateForm(instance=self.user, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('This email address is already in use.', form.errors['email'])

class UserProfileUpdateformTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='existinguser', email='existinguser@example.com', password='password123')

    def test_valid_user_profile_update_form(self):
        form_data = {
            'contact_number': '9876543210',
            'Branch': 'ICT',
        }
        form = UserProfileUpdateform(instance=self.user.profile, data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_user_profile_update_form_empty_contact_number(self):
        form_data = {
            'contact_number': '',  # Empty contact number
            'Branch': 'ICT',
        }
        form = UserProfileUpdateform(instance=self.user.profile, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('This field is required.', form.errors['contact_number'])