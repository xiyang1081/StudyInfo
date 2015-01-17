#!/usr/bin/env python
#coding=utf-8

import gevent

def foo():
	print 'runing in foo'
	gevent.sleep(0)
	print 'explicit context switch to foo again'

def bar():
	print 'runing in bar'
	gevent.sleep(0)
	print 'explicit context switch to bar again'

gevent.joinall([gevent.spawn(foo),gevent.spawn(bar),])