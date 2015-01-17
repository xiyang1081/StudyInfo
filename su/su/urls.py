#!/usr/bin/env python
#coding=utf-8
from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'su.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    #url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)

if  settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
        url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
        url(r'^(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    )
    