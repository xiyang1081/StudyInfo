#!/usr/bin/env python
#coding=utf-8

from gevent import monkey;monkey.patch_all()
import gevent
import urllib2

def f(url):
    print 'url:',url
    resp=urllib2.urlopen(url)
    data=resp.read()
    print 'url:',url,':',len(data),'bytes'

gevent.joinall([
    gevent.spawn(f,'http://www.python.org'),
    gevent.spawn(f,'http://www.baidu.com'),
    gevent.spawn(f,'http://www.zte.com.cn'),
    gevent.spawn(f,'http://www.tornadoweb.org'),
    gevent.spawn(f,'http://www.yahoo.com'),
    gevent.spawn(f,'http://github.com'),
    ])
