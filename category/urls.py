# URLconf
from django.conf.urls import include, url
from django.contrib import admin

from graino.views import *
from variety.views import *
from category.views import *
from account.views import *

# Category urls


urlpatterns = [
    url(r'^categories/$', category_list_view, name='category_list_view'),
    url(r'^categories/(?P<categ>[\w-]+)/$', category_detail, name='category_detail'),
]