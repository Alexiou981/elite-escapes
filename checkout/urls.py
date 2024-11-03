# checkout/urls.py

from django.urls import path
from .views import checkout

urlpatterns = [
    path('<int:total_price>/', checkout, name='checkout'),
]
