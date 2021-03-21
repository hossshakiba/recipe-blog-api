import os

from django.db import models
from django.contrib.auth import get_user_model

from recipe_blog.categories.models import Category
from recipe_blog.ingredients.models import Ingredient

User = get_user_model()


def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{instance.id}-{instance.title}.{ext}'

    return os.path.join('uploads/recipe/', filename)


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    instruction = models.TextField()
    time_minutes = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    ingredients = models.ManyToManyField(Ingredient)
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)

    def __str__(self):
        return self.title