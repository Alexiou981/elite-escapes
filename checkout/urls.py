# checkout/urls.py

from django.urls import path
from .views import checkout

urlpatterns = [
    path('<int:package_id>/', checkout, name='checkout'),
]
