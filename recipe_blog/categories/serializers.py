from django.utils.text import slugify

from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('name', 'slug')
        read_only_fields = ('slug', )
    
    def create(self, validated_data):
        """
        name must be capitalized & slug is name slugified
        """
        validated_data['name'] = validated_data['name'].capitalize()
        validated_data['slug'] = slugify(validated_data['name'].lower())
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        """
        Capitalize name field and update slug
        """
        instance.name = validated_data.get('name').capitalize()
        instance.slug = slugify(validated_data.get('name').lower())
        instance.save()
        return instance

    def validate_name(self, data):
        """
        Validate name if it already exists.
        Check capitalized version of name.
        """
        name = data.capitalize()
        exists = Category.objects.filter(
            name=name
        ).exists()
        if exists:
            raise serializers.ValidationError("category with this name already exists.")
        return data
