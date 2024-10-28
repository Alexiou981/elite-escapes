from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:package_id>', views.package_details, name='package_details')
]
