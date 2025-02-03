from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from home.models import Package

@login_required
def add_review(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.package = package
            review.save()
            return redirect('package_details', package_id=package.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form, 'package': package})
