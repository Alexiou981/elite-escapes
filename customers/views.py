from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
from .models import Customer
from bag.models import ShoppingCartItem


@login_required
def customer_details(request):
    """ Handle customer details submission. """
    customer = Customer.objects.filter(user=request.user).first()
    has_cart_items = ShoppingCartItem.objects.filter(
        cart__user=request.user
    ).exists()

    # Redirect user if customer details already exist
    if customer:
        return redirect(
            'order_overview' if has_cart_items else 'personal_details'
        )

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            return redirect(
                'order_overview' if has_cart_items else 'personal_details'
            )
    else:
        form = CustomerForm(instance=customer)

    return render(
        request,
        'customers/customer_details.html',
        {'form': form, 'customer': customer}
    )


@login_required
def edit_customer_details(request):
    """ Allow users to edit their saved customer details. """
    customer = get_object_or_404(Customer, user=request.user)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('personal_details')
    else:
        form = CustomerForm(instance=customer)

    return render(
        request,
        'customers/edit_customer_details.html',
        {'form': form, 'customer': customer}
    )


@login_required
def delete_customer_details(request):
    """ Allow users to delete their saved customer details. """
    customer = get_object_or_404(Customer, user=request.user)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer_details')

    return render(
        request,
        'customers/delete_customer_details.html',
        {'customer': customer}
    )


@login_required
def order_overview(request):
    """ Display the user's order summary with cart items and total price. """
    customer = get_object_or_404(Customer, user=request.user)
    cart_items = ShoppingCartItem.objects.filter(cart__user=request.user)
    total_price = sum(
        item.package.price * item.quantity for item in cart_items
    )

    return render(
        request,
        'customers/order_overview.html',
        {
            'customer': customer,
            'cart_items': cart_items,
            'total_price': total_price
        }
    )


@login_required
def personal_details(request):
    """ Display the user's saved personal details. """
    customer = Customer.objects.filter(user=request.user).first()
    return render(
        request,
        'customers/personal_details.html',
        {'customer': customer}
    )
