from rest_framework import viewsets

from .models import Ingredient
from .serializers import IngredientSerializer
from .permissions import IsCreatorOrReadOnly

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsCreatorOrReadOnly, )

    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)