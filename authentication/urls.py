from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

app_name = 'authentication'

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]
