from BeautifulSoup import BeautifulSoup
import urllib2
import sys
import threading
import Queue
import gevent
from time import sleep
import gevent.monkey
gevent.monkey.patch_all()

class Novel(object):
    def __init__(self,word,index):
        self.word = word
        self.index = index
        return
    def __cmp__(self,other):
        return cmp(self.index,other.index)

q = Queue.PriorityQueue()

def write1(url,title,index,q):
    t=1
    while t:
        try:
            f = urllib2.urlopen(url)
            t=0
        except:
            gevent.sleep(0)
    soup = BeautifulSoup(f.read().decode('gbk','ignore'))
    str1='\n'+title+'\n'+str(soup.find('dd',id='contents'))
    str1=str1.replace('&lt;br /&gt;\n&lt;br /&gt;','\n')
    str1=str1.replace('&lt;br /&gt;','\n')
    str1=str1.replace('&amp;nbsp;',' ')
    str1=str1.replace('&lt;dd id="contents"&gt;','')
    str1=str1.replace('&lt;/dd&gt;','')
    q.put(Novel(str1,index))
    print title

if __name__=='__main__':
    url = str(sys.argv[1])
    f = urllib2.urlopen(url)
    soup = BeautifulSoup(f.read().decode('gbk','ignore'))
    title = soup.title.string.split()[0]
    body = soup.findAll('td')
    str3=range(len(body))
    threads = []
    #print body.__len__()
    for i in body:
        try:
            str2=url+i.a['href']
            threads.append(gevent.spawn(write1,str2,str(i.a.string),body.index(i),q))
        except:
            pass
    gevent.joinall(threads)
    f=open(title+'.txt','wt')
    sys.stdout = f
    while not q.empty():
        print q.get().word
    f.close()
