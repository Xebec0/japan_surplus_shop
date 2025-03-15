from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryDetailView, featured_products_view

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('featured/', featured_products_view, name='featured_products'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
] 