from django.shortcuts import render, get_object_or_404
from .models import Guide


def guide_list(request):
    guides = Guide.objects.filter(is_published=True)
    return render(request, "guides/list.html", {"guides": guides})


def guide_detail(request, slug):
    guide = get_object_or_404(Guide, slug=slug, is_published=True)
    return render(request, "guides/detail.html", {"guide": guide})
