from django import template

register = template.Library()


@register.simple_tag()
def get_item(lst, index):
    try:
        return lst[int(index)]
    except IndexError:
        return None
    