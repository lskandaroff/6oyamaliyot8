from django import template

from ..models import Category, Product

register = template.Library()


@register.simple_tag
def all_categories():
    return Category.objects.all()

@register.simple_tag
def all_products():
    return Product.objects.all()
