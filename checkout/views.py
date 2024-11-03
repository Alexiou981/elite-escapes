import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from home.models import Package

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def checkout(request, total_price):
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
                        'name': 'Total Order',
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
    return render(request, 'checkout/success.html')

def cancel_view(request):
    return render(request, 'checkout/cancel.html')