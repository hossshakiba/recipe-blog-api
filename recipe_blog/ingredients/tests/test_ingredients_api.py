from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from recipe_blog.ingredients.models import Ingredient

INGREDIENT_URL = reverse('ingredients-list')


class CategoriesAPITest(TestCase):

    def setUp(self):
        """Create user & authenticate it"""
        payload = {
            'username': 'user',
            'email': 'user@test.com',
            'password': 'password',
        }
        self.user = get_user_model().objects.create_user(**payload)
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_ingredients(self):
        """Test GET/Retrieve ingredients"""
        res = self.client.get(INGREDIENT_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_ingredient(self):
        """Test create a new ingredient"""
        payload = {'name': 'salt'}
        res = self.client.post(INGREDIENT_URL, payload)
        
        exists = Ingredient.objects.filter(
            name=payload['name'],
        ).exists()

        self.assertTrue(exists)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_ingredient_invalid(self):
        """Test creating a new ingredient with invalid payload"""
        payload = {'name': ''}
        res = self.client.post(INGREDIENT_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    