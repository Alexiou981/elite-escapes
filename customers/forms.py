from django.core.validators import RegexValidator
from django import forms
from .models import Customer
from django.forms.widgets import SelectDateWidget
from datetime import datetime
from allauth.account.forms import SignupForm

class CustomerForm(forms.ModelForm):    
    phone_validator = RegexValidator(
        regex=r'^\+?\d{10,15}$',
        message="Phone number must start with '+' (optional) followed by 10-15 digits."
    )

    phone = forms.CharField(
        max_length=16,
        validators=[phone_validator],
        widget=forms.TextInput(attrs={
            'type': 'tel',
            'pattern': r'^\+?\d{10,15}$', 
            'inputmode': 'tel',
            'title': "Phone number must start with '+' (optional) followed by 10-15 digits."
        })
    )
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