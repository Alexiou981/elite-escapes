from django.db import models
from django.conf import settings


class Package(models.Model):
    ENTERTAINMENT = "Entertainment"
    RELAXATION = "Relaxation"
    EDUCATION = "Education"
    ADVENTURE = "Adventure"
    
    
    HOLIDAY_TYPE_CHOICES = [
        (ENTERTAINMENT, "Entertainment"),
        (RELAXATION, "Relaxation"),
        (EDUCATION, "Education"),
        (ADVENTURE, "Adventure"),
    ]


    name = models.CharField(max_length=255)
    brief_description = models.TextField()
    detailed_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    holiday_duration = models.PositiveIntegerField()
    date = models.DateField()
    image = models.ImageField(upload_to='package_images/', blank=True, null=True)
    holiday_type = models.CharField(max_length=25, choices=HOLIDAY_TYPE_CHOICES, default=ENTERTAINMENT)


    def __str__(self):
        return self.name


