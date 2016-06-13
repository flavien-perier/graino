from django.shortcuts import render, HttpResponse 
from django.views.generic.list import ListView 
from django.utils import timezone 
from django import forms 
from django.utils.text import slugify
 
from django.http import HttpResponse 
from django.shortcuts import render_to_response

from variety.models import *

# Category view


def category_list_view(request):
    v_categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': v_categories}, content_type='text/html')
    
def category_detail(request, categ):

    try:
        category = Category.objects.get(url=categ)
        nom_page = category.title
    
        descendant = category.get_descendants(include_self=False)
        ascendants = category.get_ancestors(ascending=False, include_self=False)
        
        categories = category.get_children()
        
        if not descendant:
            varieties = Variety.objects.filter(category__url=categ)
        else:
            varieties = Variety.objects.filter(category__in=descendant)

        return render(request, 'category_list.html', {'categories': categories, 'varieties': varieties, 'cat_parents':ascendants, 'nom_page':nom_page}, content_type='text/html')
    except:
        return render(request, '404.html', content_type='text/html')