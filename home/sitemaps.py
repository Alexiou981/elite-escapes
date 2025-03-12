from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from home.models import Package 

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return [
            'home',
            'customer_details',  
            'personal_details',
            'order_overview',
            'contact',
            'customer_bookings',
            'bag',
        ] 
    
    def location(self, item):
        return reverse(item)

class PackageSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Package.objects.all()
    
    def location(self, obj):
        return reverse('package_details', args=[obj.id]) 

    def lastmod(self, obj):
        return obj.updated_at
