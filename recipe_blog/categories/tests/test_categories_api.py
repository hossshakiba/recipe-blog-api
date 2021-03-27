from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from recipe_blog.categories.models import Category

TOKEN_URL = reverse('auth:token_obtain_pair')
CATEGORY_URL = reverse('categories-list')


class CategoriesAPITest(TestCase):

    def setUp(self):
        payload = {
            'username': 'superuser',
            'email': 'super@test.com',
            'password': 'superpass',
        }
        self.user = get_user_model().objects.create_superuser(**payload)
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_categories(self):
        """Test GET/Retrieve categories"""
        res = self.client.get(CATEGORY_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        """Test create a new category"""
        payload = {'name': 'New'}
        res = self.client.post(CATEGORY_URL, payload)
        
        exists = Category.objects.filter(
            name=payload['name'],
            slug='new',
        ).exists()

        self.assertTrue(exists)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    
    def test_create_category_invalid(self):
        """Test creating a new category with invalid payload"""
        payload = {'name': ''}
        res = self.client.post(CATEGORY_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_category(self):
        """Test updating a category"""
        payload = {'name': 'test'}
        self.client.post(CATEGORY_URL, payload)

        res = self.client.put(CATEGORY_URL + 'test/', {'name': 'new'})

        self.assertEqual(res.data['name'], 'New')
        self.assertEqual(res.data['slug'], 'new')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    

