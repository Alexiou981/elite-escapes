from django.db import models
from django.conf import settings
from home.models import Package  

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='bookings')
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    created_at = models.DateTimeField(auto_now_add=True) 


    @property
    def dates(self):
        return self.package.date
    
    @property
    def duration(self):
        return self.package.holiday_duration
    
    def __str__(self):
        return f"{self.user.username} - {self.package.name} (${self.amount})"

