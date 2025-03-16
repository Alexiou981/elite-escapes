from django import forms
from home.models import Package, PackageImages
from django.forms import inlineformset_factory

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = [
            'name', 'brief_description', 'detailed_description', 'getaway_highlights', 
            'included', 'price', 'holiday_duration', 'date', 'image', 
            'holiday_type', 'females_only'
        ]

class PackageImagesForm(forms.ModelForm):
    class Meta:
        model = PackageImages
        fields = ['image']

# Create an inline formset to handle multiple images
PackageImagesFormSet = inlineformset_factory(
    Package, PackageImages, form=PackageImagesForm, extra=3  # Allows up to 3 additional images by default
)
