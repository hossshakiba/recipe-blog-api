from rest_framework import serializers
from django.utils.text import slugify

from .models import Category



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('name', 'slug')

    def create(self, validated_data):
        """Set name as the slug if it is blank"""
        if not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)
    