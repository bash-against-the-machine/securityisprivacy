from django.shortcuts import render
from blog.models import Post
from guides.models import Guide
from news.models import NewsItem


def home(request):
    context = {
        "latest_posts": Post.objects.filter(is_published=True)[:3],
        "latest_guides": Guide.objects.filter(is_published=True)[:3],
        "latest_news": NewsItem.objects.filter(is_published=True)[:3],
    }
    return render(request, "core/home.html", context)


def about(request):
    return render(request, "core/about.html")
