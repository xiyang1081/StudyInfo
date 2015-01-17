import os,threading,sys
class test(threading.Thread):
	def __init__(self,name,delay):
		threading.Thread.__init__(self)
		self.name=name
		self.delay=delay
	def run(self):
		print self.name,self.delay
		time.sleep(self.delay)
		c=0
		while True:
			print 'This is thread %s on line %s' %(self.name,c)
			c+=1;
			if c==3:
				print 'end of thread %s' % self.name
				break
			
if __name__=='__main__':
	t1=test('Thread_01',2)
	t2=test('Thread_02',2)
	t1.start()
	print 'wait t1 to end'
	t1.join()
	t2.start()
	
	pirnt 'end of main'