from django.db import models

CATEGORY_CHOICES = [
    ('gin', 'Gin'),
    ('vodka', 'Vodka'),
    ('whiskey', 'Whiskey'),
    ('wine', 'Wine'),
]

class Category(models.Model):
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.get_friendly_name() if self.friendly_name else self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='gin')
    sku = models.CharField(max_length=20, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255, unique=False)
    description = models.TextField(blank=True)
    alcohol_percentage = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    volume_ml = models.PositiveIntegerField(null=True, blank=True, help_text="Volume in milliliters (ml)")
    price = models.DecimalField(max_digits=7, decimal_places=2)  # Supports higher prices
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name
