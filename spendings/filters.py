import django_filters as filters

from spendings.models import Spending


class SpendingFilter(filters.FilterSet):
    # Ordering by id, -id (ascending and descending)
    ordering = filters.OrderingFilter(fields={'id': 'order_id'})

    # Search by category and description, case-insensitive.
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')

    # Filtering by date: start, end, exact, start&end
    start_date = filters.DateFilter(field_name='created_at', lookup_expr='gt')
    exact_date = filters.DateFilter(field_name='created_at', lookup_expr='startswith')
    end_date = filters.DateFilter(field_name='created_at', lookup_expr='lt')

    # Filtering by amount: more than, less than, exact, more&less than
    amount_more_than = filters.NumberFilter(field_name='amount', lookup_expr='gte')
    amount_less_than = filters.NumberFilter(field_name='amount', lookup_expr='lte')
    amount_exact = filters.NumberFilter(field_name='amount', lookup_expr='exact')

    class Meta:
        model = Spending
        fields = ('amount', 'category', 'description', 'created_at')
