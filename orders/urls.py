from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # Cart URLs
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/update/<int:item_id>/', views.cart_update, name='cart_update'),
    path('cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    
    # Order URLs
    path('checkout/', views.order_create, name='order_create'),
    path('payment/<int:order_id>/', views.payment, name='payment'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
] 