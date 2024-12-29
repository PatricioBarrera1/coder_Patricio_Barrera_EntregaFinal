from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class UserTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(email="test@example.com", password="securepass123")
        self.assertEqual(user.email, "test@example.com")
