from rest_framework import serializers
from django.utils.text import slugify

from .models import Category



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('name', 'slug')

    def create(self, validated_data):
        """
        name must be capitalized & name as the slug if it is blank
        """
        validated_data['name'] = validated_data['name'].capitalize()

        if validated_data['slug']:
            validated_data['slug'] = validated_data['slug'].lower()
        else:
            validated_data['slug'] = slugify(validated_data['name'].lower())
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        """
        Lower slug field & capitalize name field after update
        """
        validated_data['name'] = validated_data['name'].capitalize()
        validated_data['slug'] = validated_data['slug'].lower()
        
        return super().update(instance, validated_data)

    