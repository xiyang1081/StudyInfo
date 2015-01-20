#!/usr/bin/env python
#coding=utf-8
import socket,select
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('',10000))
server.listen(5)
inputs=[server]
while 1:
    rs,ws,es=select.select(inputs,[],[],1)
    for r in rs:
        if r is server:
            print 'r is server'
            clientsock,clientaddr=r.accept();
            inputs.append(clientsock);
        else:
            data=r.recv(1024);
            if not data:
                inputs.remove(r);
            else:
                print data
