from rest_framework import serializers

from spendings.models import Spending, SpendingCategory


class SpendingCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SpendingCategory
        fields = ('id', 'name', 'pk')
        read_only_fields = ('id', )

    def create(self, validated_data):
        category = SpendingCategory(**validated_data)
        category.save()
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
