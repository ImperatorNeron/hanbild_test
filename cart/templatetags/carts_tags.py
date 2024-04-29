from django import template

from cart.models import Cart
from cart.utils import get_user_carts

register = template.Library()


@register.simple_tag()
def anonymous_user_carts(request):
    return get_user_carts(request)

@register.simple_tag()
def length_user_carts(request):
    return get_user_carts(request).total_quantity()