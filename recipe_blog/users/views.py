from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .serializers import UserListSerializer, UserProfileSerializer
from .permissions import IsCreator


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    permission_classes = (IsCreator, )
    search_fields = ('username', )
    ordering_fields = ('recipe', )
    lookup_field = 'username'

    def get_serializer_class(self):
        """Different serializers for different actions"""
        if self.action == 'list':
            return UserListSerializer
        return UserProfileSerializer
        