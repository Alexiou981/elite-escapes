from django.shortcuts import render, get_object_or_404
from .models import Package

# Create your views here.

def index(request):
    """ A view to return the index page """
    packages = Package.objects.all()
    return render(request, 'home/index.html', {'packages': packages})