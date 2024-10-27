from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ShoppingCart, ShoppingCartItem
from packages.models import Package

def bag(request):
    if request.user.is_authenticated:
        # For authenticated users, retrieve items from the database
        cart, created = ShoppingCart.objects.get_or_create(user=request.user)
        items = cart.items.all()
    else:
        # For non-authenticated users, retrieve items from session
        cart = request.session.get('cart', {})
        items = []
        total = 0

        # Iterate over the session cart to prepare items
        for package_id, item_data in cart.items():
            package = get_object_or_404(Package, id=package_id)
            quantity = item_data['quantity']
            total += package.price * quantity  # Calculate total price
            items.append({
                'package': package,
                'quantity': quantity,
                'get_total_price': lambda p: p.price * quantity,  # Create a lambda for total price per item
                'package_id': package_id,  # Add package_id for URL referencing
            })
    
    # Calculate the overall total for authenticated users
    if request.user.is_authenticated:
        total = sum(item.get_total_price() for item in items)

    return render(request, 'bag/bag.html', {
        'items': items,
        'total': total,
    })

def add_to_bag(request, package_id):
    package = get_object_or_404(Package, id=package_id)

    if request.user.is_authenticated:
        # For authenticated users
        cart, created = ShoppingCart.objects.get_or_create(user=request.user)

        # Add item to cart or update quantity if it exists
        item, item_created = ShoppingCartItem.objects.get_or_create(cart=cart, package=package)
        if not item_created:
            item.quantity += 1
            item.save()
    else:
        # For non-authenticated users, store in session
        cart = request.session.get('cart', {})
        if str(package_id) in cart:
            cart[package_id]['quantity'] += 1
        else:
            cart[package_id] = {'quantity': 1}
        
        # Save cart back to session
        request.session['cart'] = cart

    return redirect('bag')

def remove_from_bag(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(ShoppingCartItem, id=item_id, cart__user=request.user)
        item.delete()
    else:
        # For non-authenticated users, remove from session cart
        cart = request.session.get('cart', {})
        if str(item_id) in cart:
            del cart[str(item_id)]
            request.session['cart'] = cart

    return redirect('bag')

def update_bag_quantity(request, item_id):
    if request.user.is_authenticated:
        # Authenticated user handling
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
    else:
        # Non-authenticated user handling
        cart = request.session.get('cart', {})
        if str(item_id) in cart:
            try:
                new_quantity = int(request.POST.get('quantity', 1))
                if new_quantity < 1:
                    messages.error(request, "Quantity must be at least 1.")
                    return redirect('bag')

                cart[str(item_id)]['quantity'] = new_quantity
                request.session['cart'] = cart
                messages.success(request, "Quantity updated successfully!")
            except ValueError:
                messages.error(request, "Invalid quantity entered.")

    return redirect('bag')