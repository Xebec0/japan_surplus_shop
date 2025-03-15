import django_filters
from .models import Product, Category
from django import forms

class ProductFilter(django_filters.FilterSet):
    """
    Filter for products
    """
    name = django_filters.CharFilter(lookup_expr='icontains', label='Product Name')
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label='Category',
        empty_label='All Categories'
    )
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')
    available = django_filters.BooleanFilter(label='In Stock')
    
    class Meta:
        model = Product
        fields = ['name', 'category', 'min_price', 'max_price', 'available'] 