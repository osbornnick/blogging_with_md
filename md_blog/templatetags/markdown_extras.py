from django import template
from django.utils.safestring import mark_safe
import markdown as md


register = template.Library()


@register.filter()
def markdown(file):
    output = md.markdown(file.read(), extensions=['markdown.extensions.fenced_code'])
    return mark_safe(output)
