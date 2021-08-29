from django.urls import path

from user_profile.views import ProfileViewSet, ChangePasswordView, UpdateProfileView

app_name = 'user_profile'

urlpatterns = [
    path('', ProfileViewSet.as_view({'get': 'retrieve'}), name='user-info'),
    path('change-email/<int:pk>/', UpdateProfileView.as_view(), name='change-email'),
    path('change-password/<int:pk>/', ChangePasswordView.as_view(), name='change-password'),
    ]
