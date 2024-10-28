# views.py
from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required  # Ensure the user is logged in
def customer_details(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)  # Do not save yet
            customer.user = request.user  # Assign the logged-in user
            customer.save()  # Now save to the database

            messages.success(request, "Thank you! \
                Your details have been saved successfully!")

            return redirect('customer_details')
    else:
        form = CustomerForm()
    
    return render(request, 'customers/customer_details.html', {'form': form})
