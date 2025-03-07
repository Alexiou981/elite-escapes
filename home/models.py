from django.db import models
from tinymce.models import HTMLField

class Package(models.Model):
    ENTERTAINMENT = "Entertainment"
    RELAXATION = "Relaxation"
    EDUCATION = "Education"
    ADVENTURE = "Adventure"
    
    
    HOLIDAY_TYPE_CHOICES = [
        (ENTERTAINMENT, "Entertainment"),
        (RELAXATION, "Relaxation"),
        (EDUCATION, "Education"),
        (ADVENTURE, "Adventure"),
    ]


    name = models.CharField(max_length=255)
    brief_description = models.TextField()
    detailed_description = HTMLField(blank=True)
    getaway_highlights = HTMLField(blank=True)
    included = HTMLField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    holiday_duration = models.PositiveIntegerField()
    date = models.DateField()
    image = models.ImageField(upload_to='media/package_images/', blank=True, null=True)
    holiday_type = models.CharField(max_length=25, choices=HOLIDAY_TYPE_CHOICES, default=ENTERTAINMENT)
    females_only = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PackageImages(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='package_images/')

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email