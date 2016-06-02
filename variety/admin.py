from django.contrib import admin
from django import forms
from .models import *

from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.forms import TreeNodeChoiceField


class VarietyAdmin(admin.ModelAdmin):
    fields = ('title', 'latin', 'category', 'is_stock')
    list_display = ('title', 'category', 'is_stock')


admin.site.register(Variety, VarietyAdmin)


class CategoryAdmin(DjangoMpttAdmin):
    fields = ('title', 'parent')
    list_display = ('title', 'parent', 'level')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Group)
admin.site.register(User_group)
admin.site.register(Desire)
admin.site.register(Catalog)
admin.site.register(Desire_group)
admin.site.register(Catalog_group)
