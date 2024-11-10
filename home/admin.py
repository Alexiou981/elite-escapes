from django.contrib import admin
from .models import Package

# Registration of Package model for the admin
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date' ,'females_only')

admin.site.register(Package, PackageAdmin)

