from tinymce.widgets import TinyMCE
from django import forms
from django.contrib import admin
from .models import Package, PackageImages

class PackageAdminForm(forms.ModelForm):
    detailed_description = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Package
        fields = '__all__'

class PackageImageInline(admin.TabularInline):
    model = PackageImages
    extra = 1

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date', 'females_only')
    form = PackageAdminForm
    inlines = [PackageImageInline]
