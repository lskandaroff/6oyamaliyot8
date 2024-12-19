from django.contrib import admin
from .models import *


class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_max_show_all = 5
    actions_on_top = False
    actions_on_bottom = True
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'published', 'category')
    list_display_links = ('name', 'id')
    list_editable = ('price', 'quantity', 'published', 'category')
    list_filter = ('category', 'published')
    search_fields = ('name', 'price', 'id')
    list_per_page = 10
    actions_on_bottom = True
    actions_on_top = False
    readonly_fields = ('views',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CatAdmin)
