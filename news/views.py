from django.shortcuts import render, get_object_or_404
from .models import NewsItem


def news_list(request):
    items = NewsItem.objects.filter(is_published=True)
    return render(request, "news/list.html", {"items": items})


def news_detail(request, slug):
    item = get_object_or_404(NewsItem, slug=slug, is_published=True)
    return render(request, "news/detail.html", {"item": item})
