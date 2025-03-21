from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<int:package_id>/', views.add_to_bag, name='add_to_bag'),
    path(
        'update/<int:package_id>/',
        views.update_bag_quantity,
        name='update_bag_quantity',
    ),
]
