import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from home.models import Package
from bag.views import ShoppingCart
from bookings.models import Booking

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


def checkout(request, total_price, package_id):
    # Retrieve the selected package
    package = get_object_or_404(Package, id=package_id)

    # Save total price and package ID in session
    request.session['total_price'] = total_price
    request.session['package_id'] = package.id

    # Ensure the total is an integer representing cents
    amount_in_cents = int(float(total_price) * 100)

    # Create a new Stripe Checkout Session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': package.name,  # Use the package name for the product
                    },
                    'unit_amount': amount_in_cents,  # Total price in cents
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success')),
        cancel_url=request.build_absolute_uri(reverse('cancel')),
    )
    return redirect(session.url, code=303)

    
def success_view(request):
    # Get total price and package ID from session
    total_price = request.session.get('total_price')
    package_id = request.session.get('package_id')

    # Save the booking to the database
    if total_price and package_id and request.user.is_authenticated:
        package = get_object_or_404(Package, id=package_id)
        Booking.objects.create(
            user=request.user,
            package=package,
            amount=total_price,
        )

    # Clear session data (optional)
    request.session.pop('total_price', None)
    request.session.pop('package_id', None)

    return render(request, 'checkout/success.html')

def cancel_view(request):
    return render(request, 'checkout/cancel.html')