from django.db import models
from django.utils import timezone

class Order(models.Model):
    orderId = models.CharField(max_length=50, unique=True)
    customerName = models.CharField(max_length=255)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    posId = models.CharField(max_length=50, blank=True, null=True)
    createdAt = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20, 
        choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')],
        default='pending'
    )

    def __str__(self):
        return f"Order {self.orderId} - {self.customerName}"
