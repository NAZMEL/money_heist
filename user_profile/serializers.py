from rest_framework import serializers
from authentication.models import User


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'is_active', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True}
        }
#
#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         user = User(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user

        def update(self, instance, validated_data):
            email = validated_data.pop('email')
            user = User(**validated_data)
            user.save()

