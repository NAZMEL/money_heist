from django.urls import path

from authentication.views import TokenObtainPairView, TokenRefreshView, SignUpView, ActivateUserView

app_name = 'authentication'

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('signup/', SignUpView.as_view(), name='sign-up'),
    path('activate/', ActivateUserView.as_view(), name='user-activate'),
]
