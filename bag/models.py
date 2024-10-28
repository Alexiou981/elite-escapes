from django.db import models
from home.models import Package
from django.contrib.auth.models import User

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shopping Cart for {self.user.username}" if self.user else "Guest Cart"

class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='items')
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.package.name}"
    
    def get_total_price(self):
        return self.quantity * self.package.price

