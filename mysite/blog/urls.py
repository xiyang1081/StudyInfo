from django.conf.urls import patterns,url
from blog import views
urlpatterns=patterns('',
    url(r'^$',views.archive,name='archive'),
    url(r'^blogshow/$',views.blogShow,name='blogshow'),
    url(r'^register/$',views.register,name='register'),
    url(r'^registerUser/$',views.registerUser,name='registerUser'),
    #url(r'^(?P<poll_id>\d+)/$',views.detail,name='detail'),
    )