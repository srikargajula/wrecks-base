from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "price",
        "rating",
        "featured",
        "trending",
    )

    list_filter = (
        "category",
        "featured",
        "trending",
    )

    search_fields = (
        "title",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_editable = (
        "price",
        "featured",
        "trending",
    )
    list_display = (
        "title",
        "category",
        "price",
        "featured",
        "trending",
        "deal_of_the_day",
    )
    list_filter = (
        "category",
        "featured",
        "trending",
        "deal_of_the_day",
    )
    list_editable = (
        "price",
        "featured",
        "trending",
        "deal_of_the_day",
    )