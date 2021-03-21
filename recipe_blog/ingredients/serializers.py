from rest_framework import serializers

from .models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ingredient
        fields = ('name', 'user')
        read_only_fields = ('user',)
