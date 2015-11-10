from django import template

register = template.Library()

@register.filter
def format_number(number):
    return "{:,}".format(number)