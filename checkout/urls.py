# checkout/urls.py

from django.urls import path
from .views import checkout
from .webhooks import webhook

urlpatterns = [
    path('<int:total_price>/<int:package_id>/', checkout, name='checkout'),
    path('wh/', webhook, name='webhook'),
]
