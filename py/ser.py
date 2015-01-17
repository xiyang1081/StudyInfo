#coding=utf-8

from socket import *
import time
import threading

def answer_screen(HOST,PORT,BUFSIZE):
	ADDR=(HOST,PORT)
	tcpsersock=socket(AF_INET,SOCK_STREAM)
	tcpsersock.bind(ADDR)
	tcpsersock.listen(5)

	while True:
		print '正在连接.....................'
		tcpconn,addr=tcpsersock.accept()
		print '连接：',addr

		while True:
			data=tcpconn.recv(BUFSIZE)

			if not data:
				break
			tcpconn.send('[%s]  %s' % (time.ctime(),data))
			print [time.ctime()],':',data
	tcpconn.close()
	tcpsersock.close()

if __name__=='__main__':
	answer_screen('127.0.0.1',21567,1024)
