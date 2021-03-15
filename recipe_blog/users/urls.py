from django.urls import path
from .views import UserProfileView


urlpatterns = [
    path('<str:username>', UserProfileView.as_view(), name='profile'),
]
