from django import template

register = template.Library()

@register.filter
def linebreak_title(value):
    return value.replace('\\n', '<br>')