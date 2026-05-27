from django.contrib import admin
from .models import Guide


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "difficulty", "created_at", "is_published")
    list_filter = ("is_published", "category", "difficulty")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "body")
