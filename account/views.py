from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone
from django import forms
from django.utils.text import slugify

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import Group
from django.forms import ModelForm

from variety.models import *

# Account view

"""class ContactForm(ModelForm):
    class Meta:
        model = Profile

def singin(request):
    contact_form = ContactForm()
    return render_to_response('singin.html', {'contact_form' : contact_form})"""