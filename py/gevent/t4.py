import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2
import json
import datetime

def fetch(pid):
	req=urllib2.urlopen('http://www.zte.com.cn')
	result=req.read()
	#print result
	'''
	json_result=json.loads(result)
	print json_resoult
	datetime=json_result['datetime']
	
	print pid,datetime
	'''
	return result
	
def synchronous():
	for i in range(1,10):
		fetch(i)
		
def asychronous():
	threads=[]
	for i in range(1,10):
		threads.append(gevent.spawn(fetch,i))
	gevent.joinall(threads)
	
if __name__=='__main__':
	start=datetime.datetime.now()
	print start
	print 'synchronous'
	synchronous()
	start1=datetime.datetime.now()
	print datetime.datetime.now()-start
	print 'asychronous'
	asychronous()
	print datetime.datetime.now()- start1