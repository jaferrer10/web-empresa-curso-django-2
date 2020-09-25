from django import template
from pages.models import Page

# Registramos la función como un template tags
register = template.Library()
@register.simple_tag

def get_page_list():
    pages = Page.objects.all()
    return pages