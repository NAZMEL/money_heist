from django.urls import path
from user_profile.views import *

app_name = 'user_profile'

urlpatterns = [
    path('', ProfileViewSet.as_view({'get': 'retrieve'})),
    path('change_email/', ProfileViewSet.as_view({'patch': 'partial_update'})),
    path('get_profiles_info/', user_profiles_view)
]

