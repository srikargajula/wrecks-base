from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog_list(request):

    blogs = Blog.objects.order_by("-created_at")

    return render(request, "blog_list.html", {
        "blogs": blogs,
    })


def blog_detail(request, slug):

    blog = get_object_or_404(Blog, slug=slug)

    recent_blogs = Blog.objects.exclude(
        id=blog.id
    ).order_by("-created_at")[:4]

    return render(request, "blog_detail.html", {
        "blog": blog,
        "recent_blogs": recent_blogs,
    })