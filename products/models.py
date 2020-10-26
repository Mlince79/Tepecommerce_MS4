from django.db import models


class Product(models.Model):
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    size = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(blank=True)
    new = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
