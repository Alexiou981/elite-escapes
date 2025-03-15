from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from home.models import Package
from .forms import PackageForm

# Function to check if the user is an admin
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'role') and user.is_admin()



# Admin Dashboard - List All Packages
@login_required
def admin_dashboard(request):
    if not is_admin(request.user):
        return redirect('home')  # Redirect non-admin users to the homepage
    packages = Package.objects.all()
    return render(request, 'admin_panel/dashboard.html', {'packages': packages})

# Add Package
@login_required
def add_package(request):
    if not is_admin(request.user):
        return redirect('home')
    
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PackageForm()
    
    return render(request, 'admin_panel/add_package.html', {'form': form})

# Edit Package
@login_required
def edit_package(request, package_id):
    if not is_admin(request.user):
        return redirect('home')

    package = get_object_or_404(Package, id=package_id)
    
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PackageForm(instance=package)
    
    return render(request, 'admin_panel/edit_package.html', {'form': form, 'package': package})

# Delete Package
@login_required
def delete_package(request, package_id):
    if not is_admin(request.user):
        return redirect('home')

    package = get_object_or_404(Package, id=package_id)
    package.delete()
    return redirect('admin_dashboard')
