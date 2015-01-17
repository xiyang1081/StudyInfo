#coding=utf-8

from socket import *
from time import ctime
import threading
import sys
import select

def answer_screen(HOST,PORT,BUFSIZE):
	ADDR=(HOST,PORT)
	tcpsersock=socket(AF_INET,SOCK_STREAM)
	tcpsersock.connect(ADDR)
	reinput=[tcpsersock]

	while True:
		readInput,readOutput,readException=select.select(reinput,[],[],1)
		for indata in readInput:
			
			if indata==tcpconn:				
				data=tcpconn.recv(BUFSIZE)
				if not data:
					break
				print data
			else:
				data=raw_input('>')
				if not data:
					break
				tcpconn.send('[%s]  %s' % (time.ctime(),data))
				print [time.ctime()],':',data
	tcpconn.close()
	tcpsersock.close()

if __name__=='__main__':
	answer_screen('127.0.0.1',21567,1024)
