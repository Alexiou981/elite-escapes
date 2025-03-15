from django.db import models
from django.conf import settings

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    package = models.ForeignKey('home.Package', on_delete=models.CASCADE, related_name="reviews")  # Associated package
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5
    comment = models.TextField()  # User review text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of the review creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of the last edit

    def __str__(self):
        return f"Review by {self.user.username} for {self.package.name}"
