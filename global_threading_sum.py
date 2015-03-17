#coding=utf-8

import threading

def Cmp(sumResult):
    print 'Start cmp....'
    sumResult.start()
    sumResult.join()
    if s == 5050:
        print 'good'
    else:
        print 'bad'

    print 'End cmp....'

def SumResult():
    print 'Start sum.....'
    global s
    s=reduce(lambda x,y:x+y,xrange(1,101))
    print 'End sum.....'

if __name__=='__main__':
    s=0
    sumResult=threading.Thread(target=SumResult)
    cmp=threading.Thread(target=Cmp,args=(sumResult,))
    cmp.start()
