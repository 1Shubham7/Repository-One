from django import template
register = template.Library()

def bhatt(value,argument):
    """
    this cuts out argument from your string
    """
    return value.replace(argument,"")

register.filter('bhatt',bhatt)
