from datetime import timedelta
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user(self):
        """Test create user"""
        User = get_user_model()
        username = 'testuser'
        email = 'user@test.com'
        password = 'password'
        user = User.objects.create_user(username=username, email=email, password=password)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        """Test create super user"""
        User = get_user_model()
        username = 'superuser'
        email = 'super@test.com'
        password = 'superduperpassword'
        user = User.objects.create_superuser(username=username, email=email, password=password)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_user_email_normalized(self):
        """Test normalizing of user's email"""
        User = get_user_model()
        username = 'testuser'
        email = 'test@TEST.com'
        password = 'password'
        user = User.objects.create_user(username=username, email=email, password=password)
        self.assertEqual(user.email, email.lower())

    def test_new_user_email_required(self):
        """Test email is a required field"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(username='test', email=None, password='password')

    def test_user_is_special(self):
        """Test if is_specail_member fuction works fine for a user"""
        User = get_user_model()
        username = 'testuser'
        email = 'test@test.com'
        password = 'password'
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_special += timedelta(days=3)
        self.assertTrue(user.is_special_member())

    def test_super_user_is_special(self):
        """Test if is_specail_member fuction works fine for a superuser"""
        User = get_user_model()
        username = 'superuser'
        email = 'super@test.com'
        password = 'superduperpassword'
        user = User.objects.create_superuser(username=username, email=email, password=password)
        self.assertTrue(user.is_special_member())
