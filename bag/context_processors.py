from .models import ShoppingCart


def bag_total(request):
    if request.user.is_authenticated:
        cart, created = ShoppingCart.objects.get_or_create(user=request.user)
        total = sum(item.get_total_price() for item in cart.items.all())
    else:
        total = 0.0
    return {'grand_total': total}
