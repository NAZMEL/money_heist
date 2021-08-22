from django.urls import path
from user_profile.views import ProfileViewSet, ChangePasswordView

app_name = 'user_profile'

urlpatterns = [
    path('', ProfileViewSet.as_view({'get': 'retrieve'})),
    path('change_email/', ProfileViewSet.as_view({'patch': 'partial_update'})),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='change_password'),
    ]
