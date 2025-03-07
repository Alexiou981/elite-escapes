from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Package
from .forms import NewsletterSignupForm
# Create your views here.

def index(request):
    """ A view to return the index page and packages """
    packages = Package.objects.all()
    return render(request, 'home/index.html', {
        'packages': packages,
        'MEDIA_URL': settings.MEDIA_URL
        })


def package_details(request, package_id):
    """ A view to render the package details page """
    package = get_object_or_404(Package, id=package_id)
    reviews = package.reviews.all()  # Fetch reviews related to this package
    return render(request, 'home/package_details.html', {
        'package': package,
        'MEDIA_URL': settings.MEDIA_URL
        })


def newsletter_signup(request):
    if request.method == "POST":
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            subscriber = form.save()

            # Send confirmation email
            send_mail(
                subject="Thank You for Subscribing!",
                message="You have successfully subscribed to our newsletter. Stay tuned for updates!",
                from_email="your-email@gmail.com",  # Use the email configured in settings.py
                recipient_list=[subscriber.email],
                fail_silently=False,
            )

            messages.success(request, "Thank you for signing up! A confirmation email has been sent to your inbox.")
            return redirect("home")  # Redirect back to home page

    else:
        form = NewsletterSignupForm()

    return redirect("home")