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
        cart = request.session.get('bag', {})
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
        cart = request.session.get('bag', {})
        if str(package_id) in cart:
            cart[package_id]['quantity'] += 1
        else:
            cart[package_id] = {'quantity': 1}
        
        # Save cart back to session
        request.session['bag'] = cart

    return redirect('bag')

def remove_from_bag(request, package_id):
    if request.user.is_authenticated:
        # Retrieve the user's shopping cart
        cart = get_object_or_404(ShoppingCart, user=request.user)

        # Get the specific item from the cart
        item = get_object_or_404(ShoppingCartItem, package_id=package_id, cart=cart)
        item.delete()  # Remove the item from the shopping cart
    else:
        # For non-authenticated users, remove from session cart
        bag = request.session.get('bag', {})
        if str(package_id) in bag:
            del bag[str(package_id)]
            request.session['bag'] = bag

    return redirect('bag')

def update_bag_quantity(request, package_id):
    if request.user.is_authenticated:
        # Authenticated user handling
        # Get the user's shopping cart
        cart = get_object_or_404(ShoppingCart, user=request.user)

        # Get the specific item from the cart
        item = get_object_or_404(ShoppingCartItem, package_id=package_id, cart=cart)

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
        cart = request.session.get('bag', {})  # Use the same session key as before
        if str(package_id) in cart:
            try:
                new_quantity = int(request.POST.get('quantity', 1))
                if new_quantity < 1:
                    messages.error(request, "Quantity must be at least 1.")
                    return redirect('bag')

                # Update the quantity in the session data
                cart[str(package_id)]['quantity'] = new_quantity
                request.session['bag'] = cart
                messages.success(request, "Quantity updated successfully!")
            except ValueError:
                messages.error(request, "Invalid quantity entered.")

    return redirect('bag')