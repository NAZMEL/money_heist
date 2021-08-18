from django.urls import path
from user_profile.views import ProfileViewSet

app_name = 'user_profile'

urlpatterns = [
    path("", ProfileViewSet.as_view({"get": 'retrieve'}))
]