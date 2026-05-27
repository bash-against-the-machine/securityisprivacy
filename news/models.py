from django.db import models
from django.urls import reverse


class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    summary = models.TextField()
    source_url = models.URLField(blank=True)
    source_name = models.CharField(max_length=100, blank=True)
    published_date = models.DateField()
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:detail", kwargs={"slug": self.slug})
