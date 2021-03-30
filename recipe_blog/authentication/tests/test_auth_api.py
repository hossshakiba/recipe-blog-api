from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('auth:register')
TOKEN_URL = reverse('auth:token_obtain_pair')
REFRESH_URL = reverse('auth:token_refresh')
CHANGE_PASSWORD_URL = reverse('auth:change_password')

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class AuthenticationTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'username': 'testuser',
            'email': 'test@test.com',
            'password': 'testpass',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(username=payload['username'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creating a user that already exists fails"""
        payload = {
            'username': 'testuser',
            'email': 'test@test.com',
            'password': 'testpass',
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password must be more than 6 characters"""
        payload = {
            'username': 'testuser',
            'email': 'test@test.com',
            'password': 'passs',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = {
            'username': 'testuser',
            'email': 'test@test.com',
            'password': 'passs',
        }
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('access', res.data)
        self.assertIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that token is not created if invalid credentials are given"""
        create_user(username='testuser', email='testuser', password="testpass")
        payload = {'username': 'invalid', 'password': 'wrong'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('access', res.data)
        self.assertNotIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_token_no_user(self):
        """Test that token is not created if user doesn't exist"""
        payload = {'username': 'testuser', 'password': 'testpass'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('access', res.data)
        self.assertNotIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_refresh_token_for_user(self):
        """Test that a refresh token created for the user"""
        payload = {
            'username': 'testuser',
            'email': 'test@test.com',
            'password': 'passs',
        }
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)
        refresh = {'refresh': res.data['refresh']} 
        new_res = self.client.post(REFRESH_URL, refresh)

        self.assertIn('access', new_res.data)
        self.assertIn('refresh', new_res.data)
        self.assertEqual(new_res.status_code, status.HTTP_200_OK)

    def test_refresh_token_invalid_credentials(self):
        """Test that refresh token is not created if invalid credentials are given"""
        payload = {'refresh': 'invalidrefreshtoken'}
        res = self.client.post(REFRESH_URL, payload)

        self.assertNotIn('access', res.data)
        self.assertNotIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_change_password(self):
        """Test that user can change password"""
        payload = {
            'username': 'testuser',
            'email': 'test@test.com',
            'password': 'passs',
        }
        self.user = create_user(**payload)
        self.client = APIClient()
        self.client.force_authenticate(self.user)

        payload = {
            'old_password': 'passs',
            'new_password': 'newpass'
        }
        res = self.client.put(CHANGE_PASSWORD_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)