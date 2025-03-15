from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'title', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['product__name', 'user__username', 'title', 'comment']
    date_hierarchy = 'created_at'
    raw_id_fields = ['product', 'user']

admin.site.register(Review, ReviewAdmin)
