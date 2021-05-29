from django import template

register = template.Library()

@register.simple_tag
def addMonitor(cam):
    """Concat arg cam with monitor for url stream"""
    s = "monitor" + str(cam)
    return s
