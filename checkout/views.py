import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from home.models import Package

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def checkout(request, package_id):
    package = Package.objects.get(id=package_id)  # Fetch the package details
    if request.method == 'POST':
        # Create a new Checkout Session for the order
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': package.name,  # Package name
                        },
                        'unit_amount': int(package.price * 100),  # Price in cents
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )
        return redirect(session.url, code=303)

    return render(request, 'checkout/checkout.html', {'package': package})


def success_view(request):
    return render(request, 'checkout/success.html')

def cancel_view(request):
    return render(request, 'checkout/cancel.html')