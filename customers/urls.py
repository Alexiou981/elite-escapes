from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.customer_details, name='customer_details'),
    path(
        'edit_customer_details/',
        views.edit_customer_details,
        name='edit_customer_details'
    ),
    path(
        'delete_customer_details/',
        views.delete_customer_details,
        name='delete_customer_details'
    ),
    path('personal-details/', views.personal_details, name='personal_details'),
    path('order-overview/', views.order_overview, name='order_overview'),
]
