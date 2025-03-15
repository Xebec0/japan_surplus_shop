from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Product
from django.db.models import Q
from django_filters.views import FilterView
from .filters import ProductFilter

class ProductListView(FilterView):
    """
    View for listing all products with filtering
    """
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    filterset_class = ProductFilter
    paginate_by = 12
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(available=True)
        
        # Search functionality
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(category__name__icontains=search_query)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductDetailView(DetailView):
    """
    View for displaying product details
    """
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['related_products'] = Product.objects.filter(
            category=product.category
        ).exclude(id=product.id)[:4]
        return context

class CategoryDetailView(DetailView):
    """
    View for displaying products in a specific category
    """
    model = Category
    template_name = 'products/category_detail.html'
    context_object_name = 'category'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['products'] = Product.objects.filter(
            category=category, available=True
        )
        return context

def featured_products_view(request):
    """
    View for displaying featured products
    """
    featured_products = Product.objects.filter(featured=True, available=True)
    return render(request, 'products/featured_products.html', {
        'featured_products': featured_products
    })
