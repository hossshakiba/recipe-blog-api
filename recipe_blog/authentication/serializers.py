from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"style": {"input_type": "password"}, "write_only": True}}

    def create(self, validated_data):
        """Create a new user with validated data"""
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user