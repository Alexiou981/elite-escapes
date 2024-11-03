# views.py
from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required 
def customer_details(request):
    # Check if the current user already has a saved customer record
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        customer = None

    if request.method == 'POST':
        if customer:
            # If customer details already exist, prevent re-saving
            messages.warning(request, "You have already saved your details.")
            return redirect('personal_details')  
            
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False) 
            customer.user = request.user  
            customer.save()  

            messages.success(request, "Thank you! \
                Your details have been saved successfully!")

            return redirect('customer_details')
    else:
        form = CustomerForm()
    
    return render(request, 'customers/customer_details.html', {'form': form})


def personal_details(request):
    # Try to fetch the customer's information for the logged-in user
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        customer = None  # No details exist for this user yet

    return render(request, 'customers/personal_details.html', {
        'customer': customer
    })
