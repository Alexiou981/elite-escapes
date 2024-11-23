from django.db import models
from django.contrib.auth.models import User
from home.models import Package  

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='bookings')
    amount = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return f"{self.user.username} - {self.package.name} (${self.amount})"

