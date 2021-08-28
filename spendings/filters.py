import django_filters as filters

from .models import Spending


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class SpendingFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    ordering = filters.OrderingFilter(fields={'id': 'order_id'})
    start_date = filters.DateFilter(field_name='created_at', lookup_expr='gt')
    exact_date = filters.DateFilter(field_name='created_at', lookup_expr='startswith')
    end_date = filters.DateFilter(field_name='created_at', lookup_expr='lt')

    description = filters.CharFilter(field_name='description', lookup_expr='icontains')
    amount_more_than = filters.NumberFilter(field_name='amount', lookup_expr='gte')
    amount_less_than = filters.NumberFilter(field_name='amount', lookup_expr='lte')
    amount_exact = filters.NumberFilter(field_name='amount', lookup_expr='exact')

    class Meta:
        model = Spending
        fields = ('amount', 'category', 'description', 'created_at')
