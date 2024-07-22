"""
Test for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    """Test models."""

    def test_create_user_with_email_success(self):
        """Test creating a user with email is successfull."""

        email="test@example .com"
        pasword="asdASD123!"
        user = get_user_model().objects.create_user(
            email=email,
            password=pasword,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(pasword))
        