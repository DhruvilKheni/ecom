from atexit import register
from django import template

register = template.Library()


@register.filter(name="increment")
def increment(qty):
    return qty+1


@register.filter(name="decrement")
def decrement(qty):
    return qty-1


@register.filter(name="get_all_total")
def get_all_total(carts, ship=0):
    total = 0
    for item in carts:
        total += item.product.price*item.quantity
    return total+ship
