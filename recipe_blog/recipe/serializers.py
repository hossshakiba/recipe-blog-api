from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes"""
    url = serializers.HyperlinkedIdentityField(view_name='recipes-detail')

    class Meta:
        model = Recipe
        fields = (
            'author', 'title', 'instruction', 'time_minutes', 
            'categories', 'ingredients', 'image', 'url'
        )
        read_only_fields = ('author', )