from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
    """
    Serializer for users list-view
    """
    recipe_count = serializers.ReadOnlyField(source='recipe_set.count')
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'recipe_count', 'is_special_member')
    
    
class UserProfileSerializer(UserListSerializer):
    """
    Serializer for users' profiles
    """
    special_member_until = serializers.DateTimeField(
        source='is_special', 
        format='date: %d-%m-%Y time: %H:%M:%S',
        read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'recipe_count', 'is_special_member', 'special_member_until')


    def __init__(self, *args, **kwargs):
        """Users can see only their personal special membership duration"""
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        if self.instance != user:
            del self.fields['special_member_until']