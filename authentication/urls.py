from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authentication.models import User
from authentication import views

from django.urls import path, include
from .views import *


app_name = 'authentication'

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('register/', user_register, name='user-register'),
    path('activate/', ActivateUserView.as_view(), name='user-activate'),
]

# path('verify/', views.VerifyJSONWebToken.as_view(), name='auth-verify'),
# path('refresh/', views.RefreshJSONWebToken.as_view(), name='auth-refresh'),
# path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
# path('activate/', views.ActivateUserView.as_view(), name='activate'),
# path('reset/', views.ResetPasswordView.as_view(), name='reset'),
# path('restore/', views.RestorePasswordView.as_view(), name='restore'),
