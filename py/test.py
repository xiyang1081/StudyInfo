#!/usr/bin/env python
#coding=utf-8
class Test(object):
	"""docstring for Test"""
	def __init__(self, name):
		self.name = name
	def show(self,name2):
		print 'name:',self.name
		print 'name2',name2

t=Test('pws')
t.show('admin')
		