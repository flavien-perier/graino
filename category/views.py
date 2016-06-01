from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone
from django import forms
from django.utils.text import slugify

import mptt
from mptt.models import MPTTModel, TreeForeignKey

from django.http import HttpResponse
from django.shortcuts import render_to_response

from variety.models import Variety, Category

# Category view


def category_list_view(request):
    v_categories = Category.objects.all()
    return render_to_response('category_list.html', {'categories': v_categories})
    
def category_detail(request, category):
    page = category
    category = Category.objects.get(url=category)
    categories = category.get_children()
    descendant = category.get_descendants(include_self=False)
    varieties = Variety.objects.filter(category__in=descendant)
    ascendants = category.get_ancestors(ascending=False, include_self=False)
    return render_to_response('category_list.html', {'categories': categories, 'varieties': varieties, 'cat_parents':ascendants, 'page':page})