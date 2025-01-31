from django.shortcuts import render, get_object_or_404
from .models import Package

# Create your views here.

def index(request):
    """ A view to return the index page and packages """
    packages = Package.objects.all()
    return render(request, 'home/index.html', {'packages': packages})


def package_details(request, package_id):
    """ A view to render the package details page """
    package = get_object_or_404(Package, id=package_id)

    print(f"DEBUG: Loaded package - {package.name}")
    print(f"DEBUG: Detailed description - {package.detailed_description}")
    print(f"DEBUG: Getaway highlights - {package.getaway_highlights}")
    return render(request, 'home/package_details.html', {'package': package})