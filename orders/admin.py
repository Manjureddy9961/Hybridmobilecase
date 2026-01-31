from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'phone_brand', 'phone_model', 'quantity', 'created_at')
    list_filter = ('created_at', 'phone_brand', 'protection_level')
    search_fields = ('customer_name', 'email', 'phone_model')
    ordering = ('-created_at',)
