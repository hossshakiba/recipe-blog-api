from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
    recipe_count = serializers.SerializerMethodField()
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'recipe_count', 'is_special_member')
        read_only_fields = ('recipe_count', )

    def get_recipe_count(self, obj):
        return obj.recipe_set.count()
    
    
class UserProfileSerializer(UserListSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'recipe_count', 'is_special_member', 'special member until:')
        extra_kwargs = {
            'special member until:': {
                'format': 'date: %d-%m-%Y time: %H:%M:%S',
                'source': 'is_special'
            },
        }
        read_only_fields = ('special member until:', )

    def __init__(self, *args, **kwargs):
        """Users can see only their personal special membership duration"""
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        if self.instance != user:
            del self.fields['special member until:']