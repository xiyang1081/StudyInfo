#coding=utf-8

import gevent
import time
from gevent import select

start=time.time()
tic=lambda:'at %1.1f seconds'%(time.time())

def foo():
    print 'Running in foo %s'%(tic()-start)
    select.select([],[],[],2)
    print 'explicit context switch fo foo again',tic()

def bar():
    print 'Running in bar ',tic()
    select.select([],[],[],2)
    print 'explicit context switch fo bar again',tic()

def far():
    print 'Running in far at: ',tic()
    gevent.sleep(1)
    print 'explicit context switch fo bar again',tic()

if __name__=='__main__':
    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar),
        gevent.spawn(far),
        ])
