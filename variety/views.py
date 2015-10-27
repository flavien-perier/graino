from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone
from variety.models import Variety

# Create your views here.
def index(request):
    return HttpResponse("hello")


class VarietyListView(ListView):
    context_object_name = 'varieties'
    model = Variety
