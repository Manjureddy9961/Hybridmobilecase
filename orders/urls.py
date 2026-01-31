from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.create_order, name='order'),
    path('admin-dashboard/', views.admin_order_dashboard, name='admin_order_dashboard'),
]
