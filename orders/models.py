from django.db import models

class Order(models.Model):
    PROTECTION_LEVEL_CHOICES = [
        ('Normal', 'Normal'),
        ('Heavy', 'Heavy'),
        ('Extreme', 'Extreme'),
    ]

    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    delivery_address = models.TextField()
    
    phone_brand = models.CharField(max_length=50)
    phone_model = models.CharField(max_length=50)
    phone_size = models.CharField(max_length=20, blank=True, null=True)
    
    case_color = models.CharField(max_length=30)
    protection_level = models.CharField(max_length=20, choices=PROTECTION_LEVEL_CHOICES, default='Normal')
    quantity = models.PositiveIntegerField(default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.phone_brand} {self.phone_model} ({self.created_at.strftime('%Y-%m-%d')})"
