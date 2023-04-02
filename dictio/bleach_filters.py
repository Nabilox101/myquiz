import django_bleach

from django import template

register = template.Library()

@register.filter
def bleach_clean(value):
    return bleach.clean(value)
