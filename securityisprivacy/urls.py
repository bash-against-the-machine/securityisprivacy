from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("blog/", include("blog.urls")),
    path("guides/", include("guides.urls")),
    path("news/", include("news.urls")),
]
