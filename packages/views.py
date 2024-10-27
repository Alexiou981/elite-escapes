from django.shortcuts import render, get_object_or_404
from .models import Package

# Create your views here.

def packages(request):
    packages = Package.objects.all()
    return render(request, 'packages/packages.html', {'packages': packages})


def package_details(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    return render(request, 'packages/package_details.html', {'package': package})