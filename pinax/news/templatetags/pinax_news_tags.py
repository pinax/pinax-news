from django import template
from django.utils import timezone

from ..models import News


register = template.Library()


@register.simple_tag
def news(obj):
    """
    Usage:
        {% news as var %}
    """
    return News.objects.filter(published_at__lte=timezone.now()).order_by("-published_at")
