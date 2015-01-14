#!/usr/bin/python
#coding=utf-8

def sum(x=1,y=2):
    return x+y

def func(x):
    if x>0:
        return x
def power(x):
    return x**x
def power1(x,y):
    return x**y

def funcr(n):
    for i in range(n):
        return i

def funcy(n):
    for i in range(n):
        yield i
        


if __name__=='__main__':
    print 'This is main '
    print apply(sum,(1,3))
    print filter(func,range(-10,10))

    print reduce(sum,range(0,10))
    print reduce(sum,range(0,10),10)

    print map(power,range(1,5))

    print map(power1,range(1,5),range(1,5))


    print bool(0)

    print buffer('adbcd',1,3)

    print cmp(0,2)

    print coerce(1,2)

    print zip((1,2,3),(2,4,6))

    print 'return:',funcr(3)

    f=funcy(3)
    print f
    print f.next()
    print f.next()


    
    
