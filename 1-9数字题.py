#coding=utf-8
'''
a-b=c
d/e=f
g+h=i
c*f=i  
这几个字母是1-9 9个数字 9个数字各不相等
'''
import itertools

def func(n):
    return n[0]-n[1]==n[2] and n[3]/n[4]==n[5] and n[6]+n[7]==n[8] and n[2] * n[5]==n[8]


def run():
    for n in itertools.permutations(range(1,10)):
        if func(n):
            for i,s in zip('abcdefghi',n):
                print '%s:%s' %(i,s),
            print ''

if __name__=='__main__':
    run()
