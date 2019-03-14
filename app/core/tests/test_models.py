from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def setUp(self):
        self.User = get_user_model()

    def test_user_can_be_created_by_email(self):
        EMAIL = 'test@email.com'
        PASSWORD = 'testpass'
        user_object = self.User.objects.create_user(email=EMAIL,
                                                    password=PASSWORD)
        self.assertEqual(user_object.email, EMAIL)
        self.assertTrue(user_object.check_password(PASSWORD))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@LONDONAPPDEV.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
