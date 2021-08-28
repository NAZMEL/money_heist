from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.serializers import SignUpSerializer, ActivateUserSerializer


class ObtainJSONWebToken(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class RefreshJSONWebToken(TokenRefreshView):
    serializer_class = TokenRefreshSerializer


class SignUpView(CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny, )


class ActivateUserView(APIView):
    serializer_class = ActivateUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.activate_user()
        token = RefreshToken.for_user(user)
        return Response(data={
            'access_token': str(token.access_token),
            'refresh_token': str(token)
        }, status=status.HTTP_200_OK)
