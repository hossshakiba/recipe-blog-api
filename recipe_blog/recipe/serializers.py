from recipe_blog.recipe.models import Recipe
from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = (
            'title', 'instruction', 'time_minutes', 
            'categories', 'ingredients', 'image'
        )