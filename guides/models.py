from django.db import models
from django.urls import reverse


class Guide(models.Model):
    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    excerpt = models.CharField(max_length=300, blank=True)
    body = models.TextField()
    category = models.CharField(max_length=100, default="General")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default="medium")
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("guides:detail", kwargs={"slug": self.slug})
