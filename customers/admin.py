from django.contrib import admin
from .models import Customer


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'first_name',
        'last_name',
        'gender',
        'email',
        'phone',
        'address',
    )


admin.site.register(Customer, CustomerAdmin)
