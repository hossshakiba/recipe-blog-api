from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'special member', 'special member until:')
        extra_kwargs = {'special member until:': {
            'read_only': True,
            'format': 'date: %d-%m-%Y time: %H:%M:%S',
            'source': 'is_special'},
            'special member': {'source': 'is_special_member'},
        }

    def __init__(self, *args, **kwargs):
        """Delete special member until: field if user is not special"""
        super().__init__(*args, **kwargs)

        if not self.instance.is_special_member():
            del self.fields['special member until:']