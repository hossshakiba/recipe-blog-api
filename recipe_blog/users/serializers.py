from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'special member', 'is special user until:')
        extra_kwargs = {'is special user until:': {
            'read_only': True, 
            'format': 'date: %d-%m-%Y time: %H:%M:%S',
            'source': 'is_special'},
            'special member': {
              'source': 'is_special_member'  
            },
            }

    # def __init__(self, *args, **kwargs):
    #     """Append is_special to fields if user is special"""
    #     super().__init__(*args, **kwargs)
    #     user =  self.context['request'].user
    #     if user.is_special_member():
    #         self.fields = ('username', 'email', 'is_special', )