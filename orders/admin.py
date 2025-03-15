from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    raw_id_fields = ['product']

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_items', 'total_price', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'user__email']
    inlines = [CartItemInline]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'full_name', 'status', 'payment_method', 'payment_completed', 'total_price', 'created_at']
    list_filter = ['status', 'payment_method', 'payment_completed', 'created_at']
    search_fields = ['user__username', 'user__email', 'full_name', 'email', 'phone']
    list_editable = ['status', 'payment_completed']
    inlines = [OrderItemInline]
    fieldsets = (
        ('Customer Information', {
            'fields': ('user', 'full_name', 'email', 'phone')
        }),
        ('Shipping Information', {
            'fields': ('address', 'city', 'state', 'postal_code', 'country')
        }),
        ('Order Information', {
            'fields': ('status', 'payment_method', 'payment_completed', 'total_price')
        }),
    )

admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
