#!/usr/bin/python
#coding=utf-8
from gevent import monkey; monkey.patch_all()
import gevent
import os
import time

def showFileProperties(path,s={}):
    for root,dirs,files in os.walk(path,True):
        #print 'root:',root
        #print files
        #print dirs
        for filename in files:
            #print 'filename:',filename
            #print 'os.path:',os.path.join(root,filename)
            #o=os.path.join(root,filename)
            #print o.split('\\')[-1].split('.')[-1]
            state=os.stat(os.path.join(root,filename))
            #print 'state:',state
            #info ='文件名：'+filename+' '
            #info+='大小：'+('%d'%state[-4])
            #print info
            size=int(state[-4])
            #print size
            s[str(os.path.join(root,filename))]=size

if __name__=='__main__':
    path1=r'E:\MyWork\Python-Study'
    p1={}
    #showFileProperties(path1,p1)
    #print p1
    path2=r'E:\PYDEV'
    p2={}
    #showFileProperties(path2,p2)
    #print p2
    gevent.joinall([
        gevent.spawn(showFileProperties,path1,p1),
        gevent.spawn(showFileProperties,path2,p2),
        ])
    
    i=0
    for k in p1.keys():
        if k in p2.keys():
            if(p1[k]==p2[k]):
                i+=1

    
