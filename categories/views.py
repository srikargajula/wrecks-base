from django.shortcuts import render, get_object_or_404
from .models import Category
from products.models import Product


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)

    products = Product.objects.filter(category=category)

    context = {
        "category": category,
        "products": products,
        "categories": Category.objects.all(),
    }

    return render(request, "category.html", context)