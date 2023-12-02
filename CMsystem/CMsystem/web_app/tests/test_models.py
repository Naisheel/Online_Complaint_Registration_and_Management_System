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

class ComplaintModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.complaint = Complaint.objects.create(
            Subject='Test Subject',
            user=self.user,
            Type_of_complaint='Cafeteria',
            Description='Test Description',
            status=3
        )

    def test_complaint_creation(self):
        self.assertTrue(isinstance(self.complaint, Complaint))
        self.assertEqual(str(self.complaint), self.complaint.get_Type_of_complaint_display())

    def test_complaint_status_change(self):
        # Change complaint status and save
        self.complaint.status = 1  # Solved
        self.complaint.save()

        # Retrieve the complaint from the database and check if the status is updated
        updated_complaint = Complaint.objects.get(pk=self.complaint.pk)
        self.assertEqual(updated_complaint.status, 1)  # 1 represents 'Solved'