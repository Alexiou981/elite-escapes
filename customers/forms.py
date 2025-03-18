from django import forms
from .models import Customer
from django.forms.widgets import SelectDateWidget
from datetime import datetime
from allauth.account.forms import SignupForm

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'email', 'phone', 'address', 'city', 'country', 'postal_code']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'date_of_birth': SelectDateWidget(
                years=range(1920, datetime.now().year + 1)
            ),
        }
    
    
class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        user.username = user.email.split('@')[0]  # Assign a unique username
        user.save()
        return user