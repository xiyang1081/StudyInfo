#!/usr/bin/env python
#coding=utf-8
from django.conf.urls import patterns, include, url

from blog import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'su.views.home', name='home'),
    url(r'^home/', views.home,name='home'),
    #url(r'^index.html$', views.home,name='home'),
    url(r'^bloglist/(?P<show_id>\d+)/$',views.blogSite,name='bloglist'),
    url(r'^show/$',views.secondShow,name='show'),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^bloglist/$',views.listContent,name='blog_list'),
)
