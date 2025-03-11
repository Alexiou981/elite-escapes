from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms.widgets import SelectDateWidget

class Customer(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
        ('Other', 'Other')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=False, blank=False, default='')  
    address = models.TextField(blank=False, null=False, default='')
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES, default='Prefer not to Say')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
