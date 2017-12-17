from django import template
from django.utils import timezone

from ..models import News

register = template.Library()


@register.simple_tag
def news():
    """
    Usage:
        {% news as var %}
    """
    return News.objects.filter(press_release=False, published_at__lte=timezone.now()).order_by("-published_at")


@register.simple_tag
def press_releases():
    """
    Usage:
        {% press_releases as var %}
    """
    return News.objects.filter(press_release=True, published_at__lte=timezone.now()).order_by("-published_at")
