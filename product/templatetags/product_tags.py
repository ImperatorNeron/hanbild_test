from django import template

from product.models import Service

register = template.Library()


@register.simple_tag()
def get_item(lst, index):
    try:
        return lst[int(index)]
    except IndexError:
        return None

@register.simple_tag()
def get_services():
    return Service.objects.order_by("index_on_page")