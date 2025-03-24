from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user'
    )

    def is_admin(self):
        return self.role == 'admin'

    # Ensure a default username is generated
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email.split('@')[0]
            # Use email prefix as username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email  # Show email instead of username in admin panel


class Customer(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
        ('Other', 'Other')
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_validator = RegexValidator(
        regex=r'^\+?\d{10,15}$',  # Allow optional "+" at the beginning
        message=(
            "Phone number must start with '+' (optional) followed by "
            "10-15 digits."
        )
    )

    phone = models.CharField(
        max_length=16,  # Increased by 1 to accommodate "+"
        validators=[phone_validator],
        null=False,
        blank=False,
        default=''
    )
    address = models.TextField(blank=False, null=False, default='')
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=25,
        choices=GENDER_CHOICES,
        default='Prefer not to Say'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
