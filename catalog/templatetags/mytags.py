from django import template
from django.conf import settings
from urllib.parse import urljoin

register = template.Library()


@register.filter
def media_url(value):
    return urljoin(settings.MEDIA_URL, value)
