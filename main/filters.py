import django_filters
from .models import OrderModel

class OrderFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = OrderModel
        fields = ['min_price', 'max_price']
