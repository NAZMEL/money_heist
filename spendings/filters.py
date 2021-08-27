import django_filters as filters

from .models import Spending


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class SpendingFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains', method='get_lower_case')
    ordering = filters.OrderingFilter(fields={'id': 'order_id'})
    created_at = filters.RangeFilter()

    class Meta:
        model = Spending
        fields = ('amount', 'description', 'created_at')

    def get_lower_case(self, queryset, name, value):
        return queryset.filter(note__contains=value.lower())
