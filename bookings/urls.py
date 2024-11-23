from django.urls import path
from . import views

urlpatterns = [
    path('my-bookings/', views.customer_bookings, name='customer_bookings'),
]
