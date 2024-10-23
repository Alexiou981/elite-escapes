from django.contrib import admin
from .models import Package

# Registration of Package model for the admin
admin.site.register(Package)
