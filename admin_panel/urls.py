from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add-package/', views.add_package, name='add_package'),
    path(
        'edit-package/<int:package_id>/',
        views.edit_package,
        name='edit_package',
    ),
    path(
        'delete-package/<int:package_id>/',
        views.delete_package,
        name='delete_package',
    ),
]
