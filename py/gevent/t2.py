#!/usr/bin/env python
#coding=utf-8
import time
import gevent
from gevent import select
import socket

start =time.time()

tic=lambda :'at %1.1f seconds' % (time.time()-start)

def gr1():
	print 'started polling',tic()
	select.select([],[],[],2)
	print 'ended polling ',tic()


def gr2():
	print 'started polling',tic()
	select.select([],[],[],2)
	print 'ended polling ',tic()

def gr3():
	print 'Hey lets do some stuff while the greenlets poll,',tic()
	gevent.sleep(0)

if __name__ == '__main__':
	gevent.joinall([gevent.spawn(gr1),gevent.spawn(gr2),gevent.spawn(gr3)])