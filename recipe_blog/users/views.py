from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    UserProfileSerializer,
)


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_class = (IsAuthenticated, )
    
    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user

