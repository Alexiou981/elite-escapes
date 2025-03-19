from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from home.models import Package, PackageImages
from .forms import PackageForm, PackageImagesFormSet
import os 
from django.conf import settings  
from django.contrib import messages

# Function to check if the user is an admin
def is_admin(user):
    return user.is_authenticated and user.is_admin()

# Admin Dashboard - List All Packages
@login_required
def admin_dashboard(request):
    if not is_admin(request.user):
        return redirect('home')  # Redirect non-admin users to the homepage
    packages = Package.objects.all()
    return render(request, 'admin_panel/dashboard.html', {'packages': packages})

# Add Package View
@login_required
@user_passes_test(is_admin)
def add_package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        images_formset = PackageImagesFormSet(request.POST, request.FILES)

        if form.is_valid():
            package = form.save()  # Save the package

            # Handle Additional Images Upload
            images = request.FILES.getlist("additional_images")
            if images:
                for image_file in images:
                    PackageImages.objects.create(package=package, image=image_file)

            messages.success(request, "Package added successfully.")
            return redirect('admin_dashboard')

        else:
            messages.error(request, "There was an error adding the package. Please check the form and try again.")

    else:
        form = PackageForm()
        images_formset = PackageImagesFormSet()

    return render(request, 'admin_panel/add_package.html', {
        'form': form,
        'images_formset': images_formset
    })

# Edit Package View
@login_required
@user_passes_test(is_admin)
def edit_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)

    if request.method == "POST":
        # Handle Cover Image Removal
        if "remove_cover" in request.POST:
            if package.image:
                image_path = os.path.join(settings.MEDIA_ROOT, str(package.image))
                if os.path.exists(image_path):
                    os.remove(image_path)
                package.image.delete(save=False)
                package.image = None
                messages.success(request, "Cover image removed successfully.")

        # Handle Additional Image Removals
        delete_image_ids = request.POST.getlist("delete_images")
        if delete_image_ids:
            for image_id in delete_image_ids:
                image_obj = get_object_or_404(PackageImages, id=image_id)
                image_path = os.path.join(settings.MEDIA_ROOT, str(image_obj.image))
                if os.path.exists(image_path):
                    os.remove(image_path)
                image_obj.delete()
            messages.success(request, "Selected additional images were removed.")

        # Handle form data update
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            package = form.save()  # Save the package details

            # ✅ Handle New Additional Images Upload
            if request.FILES.getlist("additional_images"):
                for image_file in request.FILES.getlist("additional_images"):
                    PackageImages.objects.create(package=package, image=image_file)
                messages.success(request, "New additional images uploaded successfully.")

            return redirect("admin_dashboard")
        else:
            messages.error(request, "There was an error updating the package.")

    else:
        form = PackageForm(instance=package)

    return render(request, "admin_panel/edit_package.html", {"form": form, "package": package})

# Delete Package View with Confirmation
@login_required
@user_passes_test(is_admin)
def delete_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)

    if request.method == "POST":
        package.delete()
        messages.success(request, "Package deleted successfully.")
        return redirect("admin_dashboard")

    return render(request, "admin_panel/delete_package.html", {"package": package})
