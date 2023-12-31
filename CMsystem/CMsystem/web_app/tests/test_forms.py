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
    def test_invalid_user_registration_password_mismatch(self):
        form_data = {
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'newuser@example.com',
            'password1': 'securepassword123',
            'password2': 'differentpassword',  # Passwords do not match
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('The two password fields didn’t match.', form.errors['password2'])

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

class statusupdateTest(TestCase):
    def setUp(self):
        self.complaint = Complaint.objects.create(
            Subject='Test Subject',
            user=User.objects.create_user(username='testuser', password='testpassword'),
            Type_of_complaint='Cafeteria',
            Description='Test Description',
            status=3
        )
    def test_valid_status_update_form(self):
        form_data = {
            'status': 1,  # Solved
        }
        form = statusupdate(instance=self.complaint, data=form_data)
        self.assertTrue(form.is_valid())
    def test_invalid_status_update_form_invalid_status(self):
        form_data = {
            'status': 4,  # Invalid status code
        }
        form = statusupdate(instance=self.complaint, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Select a valid choice.', form.errors['status'])

class ComplaintFormTest(TestCase):
    def test_valid_complaint_form(self):
        form_data = {
            'Subject': 'Valid Subject',
            'Type_of_complaint': 'Cafeteria',
            'Description': 'Valid Description',
        }
        form = ComplaintForm(data=form_data)
        self.assertTrue(form.is_valid())
    def test_invalid_complaint_form_empty_subject(self):
        form_data = {
            'Subject': '',  # Empty subject
            'Type_of_complaint': 'Cafeteria',
            'Description': 'Valid Description',
        }
        form = ComplaintForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('This field is required.', form.errors['Subject'])
    def test_invalid_complaint_form_long_description(self):
        form_data = {
            'Subject': 'Valid Subject',
            'Type_of_complaint': 'Cafeteria',
            'Description': 'a' * 4001,  # Exceeds maximum length
        }
        form = ComplaintForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Ensure this value has at most 4000 characters (it has 4001).', form.errors['Description'])