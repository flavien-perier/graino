# Graino view
from django.conf.urls import include, url
from django.contrib import admin

from graino.views import *
from variety.views import *
from category.views import *
from account.views import *

# Graino urls


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    url(r'^aide/$', aide, name='aide'),
    url('^', include('variety.urls')),
    url('^', include('category.urls')),
    url('^', include('account.urls')),
]
