#coding=utf-8

from socket import *
import time
import threading
import sys
import select
import Queue

def answer_screen(HOST,PORT,BUFSIZE):
	ADDR=(HOST,PORT)
	tcpsersock=socket(AF_INET,SOCK_STREAM)
	tcpsersock.setblocking(False)
	#tcpsersock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

	tcpsersock.bind(ADDR)
	tcpsersock.listen(10)

	reinput=[tcpsersock]
	output=[]
	#socket:Queue
	message_queue={}
	timeout=20

	while reinput:
		print 'wating for connection.....................'
		readInput,readOutput,readException=select.select(reinput,output,reinput,timeout)
		if not (readInput or readOutput or readException):
			print "timeout!"
			break
		for s in readInput:
			if s is tcpsersock:
				tcpconn,addr=tcpsersock.accept()
				print 'connected:',addr
				tcpconn.setblocking(0)
				readInput.append(tcpconn)
				message_queue[tcpconn]=Queue.Queue()
			else:
				data=s.recv(BUFSIZE)
				if data:
					print 'recv:',data,'from',s.getpeername()
					message_queue[s].put(data)
					if s not in output:
						output.append(s)
				else:
					print 'closing ',addr
					if s in output:
						output.remove(s)
					reinput.remove(s)
					s.close()

					#remove message queue
					del message_queue[s]

			for s in readOutput:
				try:
					next_msg=message_queue[s].get_nowait()
				except Queue.Empty :
					print s.getpeername(),'queue empty'
					output.remove(s)
				else:
					print 'sending ',next_msg,'to',s.getpeername()
					s.send(next_msg)
			for s in readException:
				print 'except condition on ',s.getpeername()
				reinput.remove(s)
				if s in output:
					output.remove(s)
				s.close()
				del message_queue[s]
		
		
		
	tcpconn.close()
	tcpsersock.close()

if __name__=='__main__':
	answer_screen('127.0.0.1',21567,1024)
