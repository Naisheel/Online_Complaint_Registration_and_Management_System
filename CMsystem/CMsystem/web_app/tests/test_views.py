from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from web_app.models import Profile, Complaint
from web_app.forms import UserRegisterForm, UserProfileform, ComplaintForm
from django.core import mail
from django.contrib.messages import get_messages
from django.contrib.auth.forms import PasswordChangeForm
from unittest.mock import patch

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from web_app.models import Complaint
from django.contrib.messages import get_messages
from django.core import mail

class ViewsTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CMsystem/home.html')

    def test_aboutus_view(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CMsystem/aboutus.html')
        
    @patch('allauth.socialaccount.adapter.DefaultSocialAccountAdapter.get_provider')
    def test_login_view(self, mock_get_provider):
        # Mock the get_provider method to return a mock provider
        mock_provider = mock_get_provider.return_value
        mock_provider.get_login_url.return_value = '/mock-login-url/'

        response = self.client.get(reverse('signin'), follow=True)
        #print(response.content.decode())  # Print the actual response content

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')  # Check for the presence of a form element
        self.assertContains(response, 'id="id_username"')  # Check for the username input field

    def test_change_password_g_view(self):
        # Log in the user with a CMievance member profile
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('change_password_g'))
        self.assertEqual(response.status_code, 200)

    
    def test_login_redirect_view_student(self):
        # Log in the user with a student profile
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('login_redirect'))
        self.assertEqual(response.status_code, 302)  # Assuming a redirect for a student

    def test_login_redirect_view_non_student(self):
        # Log in the user with a non-student profile
        # Assuming you have logic to differentiate student and non-student in the login_redirect view
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('login_redirect'))
        self.assertEqual(response.status_code, 302)  # Assuming a redirect for a non-student

    def test_dashboard_view(self):
        # Assuming you have logic to differentiate student and non-student in the dashboard view
        # Log in the user with a student profile
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_change_password_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200)

    def test_complaints_view_get(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('complaints'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CMsystem/comptotal.html')
        
    def test_list_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CMsystem/Complaints.html')

    def test_allcomplaints_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('allcomplaints'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CMsystem/AllComplaints.html')

    def test_solved_view_get(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('solved'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CMsystem/solved.html')

    def tearDown(self):
        # Clean up any test data as needed
        pass















