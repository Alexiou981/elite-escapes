from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Booking


@login_required
def customer_bookings(request):
    bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-created_at')
    return render(
        request,
        'bookings/customer_bookings.html',
        {'bookings': bookings}
    )
