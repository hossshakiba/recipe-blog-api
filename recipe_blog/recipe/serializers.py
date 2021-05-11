from rest_framework import serializers

from .models import Recipe
from recipe_blog.categories.models import Category
from recipe_blog.ingredients.models import Ingredient


class ListingField(serializers.RelatedField):
    """
    Represent the name of related field instead of it's id.
    """
    def to_representation(self, value):
        """Return the name of value."""
        return value.name
    
    def to_internal_value(self, data):
        """Validate the unvalidated coming data."""
        try:
            model = self.queryset.model
            try:
                return model.objects.get(name=data)
            except KeyError:
                raise serializers.ValidationError(f'{model} is a required field.')
            except ValueError:
                raise serializers.ValidationError(f'Invalid data is provided.')
        except model.DoesNotExist:
            raise serializers.ValidationError(f'{model} does not exist.')


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes"""
    url = serializers.HyperlinkedIdentityField(view_name='recipes-detail')
    categories = ListingField(queryset=Category.objects.all(), many=True)
    ingredients = ListingField(queryset=Ingredient.objects.all(), many=True)


    class Meta:
        model = Recipe
        fields = (
            'author', 'title', 'instruction', 'time_minutes', 
            'categories', 'ingredients', 'image', 'url'
        )
        read_only_fields = ('author', )