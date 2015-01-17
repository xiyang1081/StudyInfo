import socket
import gevent
import random
import time

def task(pid):
	print time.asctime()
	gevent.sleep(random.randint(0,2)*0.001)
	print 'Task %s done' % pid
	for i in xrange(100000):
		s=i+i
	
	
def synchronous():
	for i in range(1,10):
		task(i)
		
def asynchronous():
	threads=[gevent.spawn(task,i) for i in xrange(10)]
	gevent.joinall(threads)
	
	
if __name__=='__main__':
	print time.clock()
	print 'synchronous:'
	synchronous()
	print time.clock()

	print time.clock()
	print 'asynchronous'
	asynchronous()
	print time.clock()
