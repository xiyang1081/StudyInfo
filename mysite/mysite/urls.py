#!/usr/bin/env python
#encoding=utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()
#from blog.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^blog/$',archive),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    url(r'^$','mysite.views.index',name='index'),
    url(r'^blog/', include('blog.urls')),
)
#urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
