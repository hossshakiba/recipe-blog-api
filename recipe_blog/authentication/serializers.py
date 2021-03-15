from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
        )
        extra_kwargs = {"password": {"style": {"input_type": "password"}, "write_only": True}}

    def create(self, validated_data):
        """Create a new user with validated data"""
        password = validated_data['password']
        if len(password) < 6:
            raise serializers.ValidationError(
                "This password is too short. It must contain at least 6 character.")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
