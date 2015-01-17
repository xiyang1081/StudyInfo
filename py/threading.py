import threading
import socket

class SumThread(threading.Thread):
    def __init__(self,low,high):
        super(SumThread,self).__init__()
        self.low=low
        self.high=high
        self.total=0

    def run(self):
        for i in range(self.low,self.high):
            self.total+=i

if __name__=='__main__':
    t1=SumThread(0,101)
    t2=SumThread(0,101)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print t1.total,t2.total
    result=t1.total+t2.total

    print result
