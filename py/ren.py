#!/usr/bin/env python
#coding=utf-8

import sys

sys.stdout=open(r'./hello.txt','a+')

print 'good good study'

sys.stdout.close()

sys.stdin=open('hello.txt','r')
for line in sys.stdin.readlines():
	print line