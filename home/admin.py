from django.contrib import admin
from .models import Package, PackageImages



class PackageImageInline(admin.TabularInline):
    model = PackageImages
    extra = 1


# Registration of Package model for the admin
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date' ,'females_only')
    inlines = [PackageImageInline] 

