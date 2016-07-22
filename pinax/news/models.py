from django.db import models
from django.utils import timezone

import markdown


class News(models.Model):

    image = models.ImageField(upload_to="news-images", blank=True)
    title = models.CharField(max_length=200)
    url = models.TextField()
    description = models.TextField(blank=True)
    description_html = models.TextField(blank=True, editable=False)

    press_release = models.BooleanField(default=False)

    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.description:
            self.description_html = markdown.markdown(self.description)
        return super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "news"
