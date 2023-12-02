from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from CMsystem.models import Profile, Complaint


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(
            user=self.user,
            contact_number='1234567890',
            profile_pic=SimpleUploadedFile("test_image.jpg", content=b"file_content"),
            type_user='student',
            Branch='ICT'
        )

    def test_profile_creation(self):
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertEqual(str(self.profile), self.user.username)
