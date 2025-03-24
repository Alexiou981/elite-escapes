from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path(
        'packages/<int:package_id>',
        views.package_details,
        name='package_details'
    ),
    path(
        'newsletter-signup/',
        views.newsletter_signup,
        name="newsletter_signup"
    ),
]
