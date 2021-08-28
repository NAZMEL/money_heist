from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from authentication.models import User
from user_profile.serializers import UserSerializer, ChangePasswordSerializer, UpdateUserSerializer


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """
    Takes a set of user credentials along with the JWT token.
    Returns the user profile fields: id, email, is_active
    """
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        return self.request.user


class ChangePasswordView(generics.UpdateAPIView):
    """
    Takes the JWT token for authorization along with old password
    and new password entered 2 times. Old_password must be valid,
    and password1 equal to password2.
    Returns the user profile fields: id, email, is_active
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class UpdateProfileView(generics.UpdateAPIView):
    """
    Takes the JWT token for authorization along with
    password and new email address.
    Returns the new email.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
