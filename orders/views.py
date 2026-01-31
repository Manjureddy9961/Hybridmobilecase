from django.shortcuts import render, redirect

from django.contrib import messages
from .models import Order

import csv
import os
from django.conf import settings

def create_order(request):
    if request.method == 'POST':
        try:
            # Create Order in DB
            order = Order.objects.create(
                customer_name=request.POST.get('customer_name'),
                email=request.POST.get('email'),
                mobile_number=request.POST.get('mobile_number'),
                delivery_address=request.POST.get('delivery_address'),
                phone_brand=request.POST.get('phone_brand'),
                phone_model=request.POST.get('phone_model'),
                phone_size=request.POST.get('phone_size'),
                case_color=request.POST.get('case_color'),
                protection_level=request.POST.get('protection_level'),
                quantity=request.POST.get('quantity')
            )

            # --- Excel/CSV Export Logic ---
            file_path = os.path.join(settings.BASE_DIR, 'orders_data.csv')
            file_exists = os.path.isfile(file_path)

            with open(file_path, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Write header if file is new
                if not file_exists:
                    writer.writerow(['Order ID', 'Date', 'Customer Name', 'Email', 'Mobile', 'Address', 'Brand', 'Model', 'Size', 'Color', 'Level', 'Qty'])
                
                # Write data row
                writer.writerow([
                    order.id,
                    order.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    order.customer_name,
                    order.email,
                    order.mobile_number,
                    order.delivery_address,
                    order.phone_brand,
                    order.phone_model,
                    order.phone_size,
                    order.case_color,
                    order.protection_level,
                    order.quantity
                ])
            # ------------------------------

            messages.success(request, 'Your order has been placed successfully!')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Error placing order: {str(e)}')
            return redirect('order')
    
    return render(request, 'order.html')

def admin_order_dashboard(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'admin_orders.html', {'orders': orders})
