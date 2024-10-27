from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.packages, name='packages'),
    path('<int:package_id>', views.package_details, name='package_details')
]