from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegistrationView, ChangePasswordView

app_name = 'auth'
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password')
]
