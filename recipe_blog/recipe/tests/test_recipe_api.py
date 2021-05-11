from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from recipe_blog.recipe.models import Recipe
from recipe_blog.categories.models import Category
from recipe_blog.ingredients.models import Ingredient


RECIPE_URL = reverse('recipes-list')


class RecipesAPITest(TestCase):

    def setUp(self):
        """Create superuser & authenticate it"""
        payload = {
            'username': 'testuser',
            'email': 'test@test.com',
            'password': 'password',
        }
        self.user = get_user_model().objects.create_user(**payload)
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_recipes(self):
        """Test GET/Retrieve recipes"""
        res = self.client.get(RECIPE_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_recipe(self):
        """Test create a new recipe"""
        payload_category = {'name': 'persian'}
        Category.objects.create(**payload_category) # create a new category

        payload_ingredient = {'name': 'salt'}
        Ingredient.objects.create(**payload_ingredient) # create a new ingredient

        payload_recipe = {
            'title': 'test recipe',
            'instruction': 'this is a test recipe.',
            'time_minutes': 5,
            'categories': 'persian',
            'ingredients': 'salt'
            }
        res = self.client.post(RECIPE_URL, payload_recipe)

        exists = Recipe.objects.filter(
            title=payload_recipe['title'],
            instruction__iexact=payload_recipe['instruction'],
        ).exists()

        self.assertTrue(exists)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

