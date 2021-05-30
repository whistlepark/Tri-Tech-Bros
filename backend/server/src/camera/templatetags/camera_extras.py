from django import template

register = template.Library()

@register.filter(name='prepend')
def prepend(cam,target):
    """Concat arg cam with monitor for url stream"""
    s = target + str(cam)
    return s
