from django.db import models
from tinymce.models import HTMLField

class Package(models.Model):
    # Holiday Type Choices
    ADVENTURE = "Adventure"
    RELAXATION = "Relaxation"
    CULTURAL = "Cultural"
    WILDLIFE = "Wildlife"
    ROMANTIC = "Romantic"
    FAMILY = "Family"
    OTHER = "Other"

    HOLIDAY_TYPE_CHOICES = [
        (ADVENTURE, "Adventure"),
        (RELAXATION, "Relaxation"),
        (CULTURAL, "Cultural"),
        (WILDLIFE, "Wildlife"),
        (ROMANTIC, "Romantic"),
        (FAMILY, "Family"),
        (OTHER, "Other"),
    ]

    # Package Fields
    name = models.CharField(max_length=255)
    brief_description = models.TextField()
    detailed_description = HTMLField(blank=True)
    getaway_highlights = HTMLField(blank=True)
    included = HTMLField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    holiday_duration = models.PositiveIntegerField()
    date = models.DateField()
    image = models.ImageField(upload_to='package_images/', blank=True, null=True)
    holiday_type = models.CharField(max_length=25, choices=HOLIDAY_TYPE_CHOICES, default=ADVENTURE)
    females_only = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PackageImages(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='package_images/')

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email