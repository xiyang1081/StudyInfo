#coding=utf-8
import urllib2
import gevent
import time
import random


#imgurl="http://dl.bizhi.sogou.com/images/2014/05/04/601509.jpg"
def worker(i):
	gevent.sleep(random.randint(0,2)*0.001)
	#time=time.asctime()  
	print i,'==',time.asctime()
	imgurl="http://dl.bizhi.sogou.com/images/2014/05/04/%s.jpg" % i
	print imgurl
	try:
		s=urllib2.urlopen(urllib2.Request(imgurl))
		print s
	except IOError:
		print 'job None'
		return 	

	data=s.read()
	print "downloading...."
	path="./path/%s.jpg" % i
	with open(path,"wb") as jpg:
		jpg.write(data)
	print 'Success!'
	s.close()

if __name__=='__main__':
	threads=[gevent.spawn(worker,i) for i in xrange(500000,1000000)]
	print threads
	gevent.joinall(threads)