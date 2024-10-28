from django.db import models
from django.conf import settings

class Package(models.Model):
    name = models.CharField(max_length=255)
    brief_description = models.TextField()
    detailed_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    holiday_duration = models.PositiveIntegerField()
    destination = models.CharField(max_length=255)
    date = models.DateField()
    image = models.ImageField(upload_to='package_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


