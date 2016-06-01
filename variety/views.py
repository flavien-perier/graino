from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone
from django import forms
from django.utils.text import slugify

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import Group

from variety.models import Variety, Category

# Variety view


def variety_list_view(request):
    v_variety = Variety.objects.all()
    return render_to_response('variety_list.html', {'varieties': v_variety})

def update(request):
    for o in Category.objects.all():
        o.url = slugify(o.title)
        o.save()