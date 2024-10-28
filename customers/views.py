from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomerForm

@login_required
def customer_details(request):
    # Check if the user already has a customer profile
    try:
        customer = request.user.customer
    except Customer.DoesNotExist:
        customer = None

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            messages.success(request, "Your details have been successfully saved.")
            return redirect('customer_details')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'customers/customer_details.html', {'form': form})