#coding=utf-8
from socket import *
def answer_client(HOST,PORT,BUFSIZE):
	ADDR=(HOST,PORT)
	tcpconn=socket(AF_INET,SOCK_STREAM)
	tcpconn.connect(ADDR)

	while True:
		data=raw_input('>')
		if not data:
			break
		tcpconn.send(data)
		data=tcpconn.recv(BUFSIZE)
		if not data:
			break
		print data
	tcpconn.close()

if __name__ == '__main__':
	answer_client('127.0.0.1',21567,1024)