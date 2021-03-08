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