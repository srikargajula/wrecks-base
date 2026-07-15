from django.db import models
from categories.models import Category


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to="products/")

    affiliate_link = models.URLField()

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=5.0
    )

    featured = models.BooleanField(default=False)

    trending = models.BooleanField(default=False)

    deal_of_the_day = models.BooleanField(default=False)

    def __str__(self):
        return self.title