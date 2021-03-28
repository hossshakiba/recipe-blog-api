from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = (
            'author', 'title', 'instruction', 'time_minutes', 
            'categories', 'ingredients', 'image'
        )
        read_only_fields = ('author', )