from django import template
from django.utils.safestring import mark_safe
import markdown as md


register = template.Library()


@register.filter()
def markdown(file):
    decoded = file.read().decode('utf-8')
    extensions = ['markdown.extensions.fenced_code', 'codehilite']
    output = md.markdown(decoded, extensions=extensions)
    return mark_safe(output)
