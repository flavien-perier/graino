# -*- coding: utf-8 -*-

# URLconf
from django.conf.urls import include, url
from django.contrib import admin

from graino.views import *
from variety.views import *
from category.views import *
from account.views import *

# Variety urls


urlpatterns = [
    url(r'^add_variety/$', add_variety, name='add_variety'),
    url(r'^variety_inventory/$', variety_inventory, name='variety_inventory'),
]