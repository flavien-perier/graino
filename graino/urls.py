# Graino view
from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from graino.views import *
from variety.views import *
from category.views import *
from account.views import *

# Graino urls


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aide/$', aide, name='aide'),
    
    url(r'^profile/$', TemplateView.as_view(template_name='profile.html'), name='user_profile'),
    url('^', include('django.contrib.auth.urls')),
    
    url('^', include('variety.urls')),
    url('^', include('category.urls')),
    url('^', include('account.urls')),
]
