from atexit import register
from django import template

register = template.Library()


@register.filter("increment")
def increment():
    return 1


@register.filter("decrement")
def decrement(qty):
    return qty-1
