from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from user_profile.serializers import UserSerializer


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):

    #permission_classes = (IsAuthenticated, )
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
