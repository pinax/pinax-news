from django.contrib import admin

from .models import News


admin.site.register(News, fields=["image", "title", "url", "description", "published_at", "created_at"])
