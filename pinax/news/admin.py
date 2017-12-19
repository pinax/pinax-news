from django.contrib import admin

from .models import News

admin.site.register(News, list_display=["title", "image", "url", "description", "published_at", "created_at"])
