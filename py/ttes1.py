
class Fo(object):
    def __new__(cls, *args, **kwargs):
        print 'hi, i am Fo'
        return  super(Fo, cls).__new__(cls, *args, **kwargs)  
class Foo(Fo):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            print Foo is cls
            print issubclass(cls, Fo)
            print issubclass(cls, object)
            cls.__instance = super(Foo, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
    def hi(self):
         print 'hi, world'
if __name__ == '__main__':
    foo1 = Foo()
    foo1.hi()
    print isinstance(foo1, Foo)
    print isinstance(foo1, Fo)
    print isinstance(foo1, object) 
