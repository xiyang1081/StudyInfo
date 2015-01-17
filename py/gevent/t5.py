import gevent
from gevent import Greenlet
import socket

def foo(message,n):
	gevent.sleep(n)
	print message
	
thread1=Greenlet.spawn(foo,"hello",1)

thread2=gevent.spawn(foo,"I love!",1)

thread3=gevent.spawn(lambda x:(x+1),1)

threads=[thread1,thread2,thread3]

gevent.joinall(threads)