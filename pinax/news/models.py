import uuid

from django.db import models
from django.utils import timezone

import markdown
from imagekit.models import ImageSpecField


def image_upload_to(instance, filename):
    uid = str(uuid.uuid4())
    ext = filename.split(".")[-1].lower()
    return "news-images/{}/{}.{}".format(instance.pk, uid, ext)


class News(models.Model):

    image = models.ImageField(upload_to=image_upload_to, blank=True)
    secondary_image = models.ImageField(upload_to=image_upload_to, blank=True)
    title = models.CharField(max_length=200)
    url = models.TextField()
    description = models.TextField(blank=True)
    description_html = models.TextField(blank=True, editable=False)

    press_release = models.BooleanField(default=False)

    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    image_thumb = ImageSpecField(source="image", id="pinax_news:image:thumb")
    secondary_image_thumb = ImageSpecField(source="secondary_image", id="pinax_news:secondary_image:thumb")

    def save(self, *args, **kwargs):
        if self.description:
            self.description_html = markdown.markdown(self.description)
        return super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "news"
