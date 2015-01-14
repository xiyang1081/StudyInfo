op='+'
x=1
y=2

def switch(t,x,y):
    result={'+':x+y,
            '-':x-y,
            '*':x*y,
            '/':x/y
            }
    print result.get(t)
        
    
switch(op,x,y)
