# URLconf
from django.conf.urls import include, url
from django.contrib import admin

from graino.views import *
from variety.views import *
from category.views import *

urlpatterns = [
    url(r'^categories/$', category_list_view, name='category_list_view'),
]