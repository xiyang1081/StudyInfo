#!/usr/bin/python
#coding=utf-8
from gevent import monkey
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
    path1=r'E:\MyWork'
    p1={}
    #showFileProperties(path1,p1)
    #print p1
    path2=r'D:\Django'
    p2={}
    #showFileProperties(path2,p2)
    #print p2
    if path1==path2:
        print '文件路径相同'
        exit()
    gevent.joinall([
        gevent.spawn(showFileProperties,path1,p1),
        gevent.spawn(showFileProperties,path2,p2),
        ])
    
    i=0
    st=['pdf','rar','zip']
    li=[]
    for m in p1.keys():
        if m.split('\\')[-1].split('.')[-1] in st:
            mt=m.split('\\')[-1]
            for n in p2.keys():
                if n.split('\\')[-1].split('.')[-1] in st:                    
                    nt=n.split('\\')[-1]
                    if(mt==nt and p1[m]==p2[n]):
                        print mt,':',m
                        print mt,':',n
                        i=i+1
                        #os.remove(n)
                        li.append(n)
    if i==0:
        print '没有重复文件'
        exit()
    else:
        print '相同文件共：',i,'个'
        print '你确定要删除重复文件吗？'
        ans=raw_input('确定：Y，取消：N')
        if ans=='Y' or ans=='y':
            for j in range(len(li)):
                os.remove(li[j])
        if ans=='N' or ans=='n':
            exit()
    
