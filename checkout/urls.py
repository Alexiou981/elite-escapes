# checkout/urls.py

from django.urls import path
from .views import checkout
from .webhook_handler import stripe_webhook

urlpatterns = [
    path('<int:total_price>/<int:package_id>/', checkout, name='checkout'),
    path('webhook/stripe/', stripe_webhook, name='stripe-webhook'),
]
