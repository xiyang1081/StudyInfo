#/usr/bin/python
#coding=utf-8

def SameCount(t):
    q={}
    #q的值全部置为0
    for k in list(set(t)):
        q.setdefault(k,0)
    #统计个数
    for i in range(len(t)-1):
        q[t[i]]=q[t[i]]+1
    #根据值倒序排列
    q=sorted(q.iteritems(),key=lambda q:q[1],reverse=True)
    #判断是否有出现次数相同的
    for l in range(len(q)-1):
        if q[0][1]==q[l][1]:
            print q[l],
        else:
            break    

if __name__=='__main__':
    s='afsafdsafsdfdsgsdgsdfgfdjhfasdafsadfsadf'
    SameCount(s)
