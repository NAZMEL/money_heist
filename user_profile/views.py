from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from authentication.models import User
from user_profile.serializers import UserSerializer

from rest_framework.decorators import action, api_view, permission_classes
from rest_framework import permissions


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            # send_email_confirmation(user=self.request.user, modified=instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ProfileUpdateView()
#
#     # def perform_update(self, serializer_class):
#     #     serial.save()
#
#     instance = self.get_object()
#     serializer = self.get_serializer(instance, data=request.data, partial=partial)
#     serializer.is_valid(raise_exception=True)
#     self.perform_update(serializer)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def user_profiles_view(request):
    '''
    Get Users info
    '''
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)





