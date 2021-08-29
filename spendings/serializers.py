from django.db import IntegrityError
from rest_framework import serializers

from authentication.models import User
from spendings.models import Spending, SpendingCategory


class SpendingCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SpendingCategory
        fields = ('id', 'name', 'pk')
        read_only_fields = ('id', )

    def create(self, validated_data):

        try:
            category = SpendingCategory(**validated_data)
            category.save()

        # Exception that checks if the category name exists for a specific user
        except IntegrityError as err:
            name_category = validated_data.get('name')
            user_id = validated_data.get('user').pk
            user = User.objects.get(pk=user_id)

            raise serializers.ValidationError(f"The {name_category} already exists for {user.email}!")

        return category


class SpendingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spending
        fields = ('id', 'amount', 'description', 'category', 'created_at')
        read_only_fields = ('id',)

    def create(self, validated_data):
        spending = Spending(**validated_data)
        spending.save()
        return spending
