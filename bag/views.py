from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ShoppingCart, ShoppingCartItem
from packages.models import Package

def bag(request):
    # Retrieve or create a shopping cart
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = sum(item.get_total_price() for item in items)

    return render(request, 'bag/bag.html', {
        'items': items,
        'total': total,
    })

def add_to_bag(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)

    # Add item to cart or update quantity if it exists
    item, item_created = ShoppingCartItem.objects.get_or_create(cart=cart, package=package)
    if not item_created:
        item.quantity += 1
        item.save()
    
    return redirect('bag')

def remove_from_bag(request, item_id):
    item = get_object_or_404(ShoppingCartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('bag')


def update_bag_quantity(request, item_id):
    item = get_object_or_404(ShoppingCartItem, id=item_id, cart__user=request.user)
    
    # Get the quantity from the form data and validate it
    try:
        new_quantity = int(request.POST.get('quantity', 1))
        if new_quantity < 1:
            messages.error(request, "Quantity must be at least 1.")
            return redirect('bag')
    except ValueError:
        messages.error(request, "Invalid quantity entered.")
        return redirect('bag')
    
    # Update the quantity and save
    item.quantity = new_quantity
    item.save()
    
    messages.success(request, "Quantity updated successfully!")
    return redirect('bag')