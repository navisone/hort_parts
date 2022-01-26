from django import template
from ..models import Category, Content


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_about():
    return Content.objects.filter(category_id=1)


@register.simple_tag()
def get_warranty():
    return Content.objects.filter(category_id=2)
