from rest_framework import viewsets

from .models import Recipe
from .serializers import RecipeSerializer
from .permissions import IsCreatorOrReadOnly

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsCreatorOrReadOnly, )

    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(author=self.request.user)