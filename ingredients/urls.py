from rest_framework.routers import SimpleRouter
from .views import IngredientViewSet

router = SimpleRouter()
router.register('', IngredientViewSet, basename='ingredients')

urlpatterns = router.urls
