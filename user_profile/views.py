from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from authentication.models import User

from user_profile.serializers import UserSerializer


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #
    #     return self.update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# class ProfileUpdateView()
#
#     # def perform_update(self, serializer_class):
#     #     serial.save()
#
#     instance = self.get_object()
#     serializer = self.get_serializer(instance, data=request.data, partial=partial)
#     serializer.is_valid(raise_exception=True)
#     self.perform_update(serializer)

