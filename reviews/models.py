from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who wrote the review
    package = models.ForeignKey('home.Package', on_delete=models.CASCADE, related_name="reviews")  # Associated package
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5
    comment = models.TextField()  # User review text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of the review creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of the last edit

    def __str__(self):
        return f"Review by {self.user.username} for {self.package.name}"
