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

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@Example.COM', 'test4@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)
            