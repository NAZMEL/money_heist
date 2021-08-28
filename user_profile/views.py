from rest_framework import viewsets, status, mixins, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from authentication.models import User
from user_profile.serializers import UserSerializer, ChangePasswordSerializer, UpdateUserSerializer


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.id)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordView(generics.UpdateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.id)


class UpdateProfileView(generics.UpdateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.id)
