"""elite_escapes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from checkout.views import success_view, cancel_view
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import StaticViewSitemap, PackageSitemap
from django.conf.urls import handler404
from .views import custom_404_view

handler404 = custom_404_view

sitemaps = {
    'static': StaticViewSitemap(),
    'packages': PackageSitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('bag/', include('bag.urls')),
    path('customers/', include('customers.urls')),
    path('checkout/', include('checkout.urls')),
    path('success/', success_view, name='success'),
    path('cancel/', cancel_view, name='cancel'),
    path('bookings/', include('bookings.urls')),
    path('reviews/', include('reviews.urls')),
    path('contact/', include('contact.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('admin-panel/', include('admin_panel.urls')),
    # Sitemap URL
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
