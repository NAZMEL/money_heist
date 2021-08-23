from rest_framework import serializers
from spendings.models import Spending, SpendingCategory


class SpendingCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SpendingCategory
        fields = ('id', 'name')
        read_only_fields = ('id',)


class SpendingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spending
        fields = ('id', 'amount', 'date', 'description', 'category')
        read_only_fields = ('id',)

