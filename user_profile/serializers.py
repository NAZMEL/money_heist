from rest_framework import serializers
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', "email", "is_active", "password")
        read_only_fields = ("id", "is_active")
        write_only_fields = ("password")
