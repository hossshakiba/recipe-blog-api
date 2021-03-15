from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    UserProfileSerializer,
)
from .permissions import IsCreator


class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsCreator, )
    lookup_field = 'username'
    