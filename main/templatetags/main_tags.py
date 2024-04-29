from django import template

register = template.Library()

@register.simple_tag()
def get_cookies(request, key):
    return request.COOKIES.get(key, None)