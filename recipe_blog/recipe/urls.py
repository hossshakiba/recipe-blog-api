from rest_framework.routers import SimpleRouter

from .views import RecipeViewSet

router = SimpleRouter()
router.register('', RecipeViewSet, basename='recipes')

urlpatterns = router.urls
