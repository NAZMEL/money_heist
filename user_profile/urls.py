from django.urls import path
from user_profile.views import ProfileViewSet, ChangePasswordView, UpdateProfileView

app_name = 'user_profile'

urlpatterns = [
    path('', ProfileViewSet.as_view({'get': 'retrieve'})),
    path('change_email/<int:pk>/', UpdateProfileView.as_view(), name='change_email'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='change_password'),
    ]
