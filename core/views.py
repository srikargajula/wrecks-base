from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from products.models import Product
from categories.models import Category


def home(request):

    search = request.GET.get("search")
    category_slug = request.GET.get("category")
    sort = request.GET.get("sort")
    filter_type = request.GET.get("filter")

    products = Product.objects.all().order_by("-id")
    all_products = Product.objects.all().order_by("-id")
    categories = Category.objects.all()

    # Search
    if search:
        products = products.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )

    # Category Filter
    if category_slug:
        products = products.filter(category__slug=category_slug)

    # Special Filters
    if filter_type == "trending":
        products = products.filter(trending=True)

    elif filter_type == "featured":
        products = products.filter(featured=True)

    elif filter_type == "deal":
        products = products.filter(deal_of_the_day=True)

    # Sorting
    if sort == "low":
        products = products.order_by("price")

    elif sort == "high":
        products = products.order_by("-price")

    elif sort == "new":
        products = products.order_by("-id")

    # Trending Products
    trending_products = Product.objects.filter(trending=True)[:4]

    # Featured Products
    featured_products = Product.objects.filter(featured=True)

    # Deal of the Day
    deal_product = Product.objects.filter(deal_of_the_day=True).first()

    # Pagination
    paginator = Paginator(products, 9)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    context = {
        "products": products,
        "all_products": all_products,
        "featured_products": featured_products,
        "categories": categories,
        "trending_products": trending_products,
        "deal_product": deal_product,
    }

    # TEMPORARY DEBUG
    print("Search:", search)
    print("Products Found:", products.object_list)

    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")