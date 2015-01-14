#!/usr/bin/env python
#coding=utf-8

import urllib

fp=urllib.urlopen('https://www.python.org//')

op=open('python.html','wb')

n=0
while True:
    s=fp.read(1024)
    if not s:
        break
    op.write(s)
    n+=len(s)

fp.close()
op.close()

print n,fp.url
