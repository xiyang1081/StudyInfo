#!/usr/bin/env python
#coding=utf-8

class Ve(object):
    def __init__(self):
        print 'Ve'
    def say(self):
        print 'say Ve'

class Vs(object):
    def __init__(self):
        print 'Vs'
    def say(self):
        print 'say Vs'
    def show(self):
        print 'show Vs'
class Water(Ve,Vs):
    pass
if __name__=='__main__':
    w=Water()
    w.say()
    w.show()
