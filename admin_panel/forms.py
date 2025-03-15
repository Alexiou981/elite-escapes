from django import forms
from home.models import Package

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'price', 'brief_description', 'detailed_description', 'getaway_highlights', 'image']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter package name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter price'}),
            'brief_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter package brief description'}),
            'detailed_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter package detailed description'}),
            'getaway_highlights': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter package highlights'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
