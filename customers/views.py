# views.py
from django.shortcuts import render, redirect, get_object_or_404
from bag.views import ShoppingCart, ShoppingCartItem
from .forms import CustomerForm
from .models import Customer
from bag.models import ShoppingCartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required 
def customer_details(request):
    # Check if the current user already has a saved customer record
    customer = Customer.objects.filter(user=request.user).first()

    # Check if there are items in the shopping cart
    has_cart_items = ShoppingCartItem.objects.filter(cart__user=request.user).exists()


    if request.method == 'POST':
        if customer:
            # If customer details already exist, prevent re-saving
            messages.warning(request, "You have already saved your details.")
            return redirect('order_overview' if has_cart_items else 'personal_details')  # Redirect to order overview
            
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False) 
            customer.user = request.user  
            customer.save()  

            messages.success(request, "Thank you! Your details have been saved successfully!")

            return redirect('order_overview' if has_cart_items else 'personal_details')  # Redirect to order overview
    else:
        form = CustomerForm(instance=customer) if customer else CustomerForm()

    return render(request, 'customers/customer_details.html', {
        'form': form,
        'customer': customer
        })


@login_required
def order_overview(request):
    customer = Customer.objects.get(user=request.user)
    cart_items = ShoppingCartItem.objects.filter(cart__user=request.user)
    total_price = sum(item.package.price * item.quantity for item in cart_items)

    # Debugging prints
    for item in cart_items:
        print(f"Item: {item}, Package ID: {item.package.id if item.package else 'None'}")

    return render(request, 'customers/order_overview.html', {
        'customer': customer,
        'cart_items': cart_items,
        'total_price': total_price
    })


def personal_details(request):
    # Try to fetch the customer's information for the logged-in user
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        customer = None  # No details exist for this user yet

    return render(request, 'customers/personal_details.html', {
        'customer': customer
    })
