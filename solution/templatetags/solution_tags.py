from django import template

from solution.models import Solution

register = template.Library()

@register.simple_tag()
def get_services():
    return Solution.objects.filter().order_by("index_on_page")