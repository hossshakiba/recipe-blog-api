from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={"input_type":"password"}, required=True)
    password2 = serializers.CharField(
        style={"input_type":"password"}, required=True, label="Confirm password")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True},
                        "password2": {"write_only": True}}

    def create(self, **validated_data):
        """Create a new user with validated data"""
        password = validated_data["password"]
        password2 = validated_data["password2"]
        
        if password != password2:
            raise serializers.ValidationError(
                {"password": "The two passwords differ."})
        
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user