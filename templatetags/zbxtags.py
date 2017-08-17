from django.template import Library
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup
register = Library()

@register.simple_tag
def get_url(data):


    return '/static/case/xqds.jpg'
