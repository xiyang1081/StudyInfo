
class Foo(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        print 'hhhhhhhhh'
        if not cls.__instance:
            cls.__instance = super(Foo, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
    def sayHi(self):
        print 'Hello'
if __name__ == '__main__':
    foo1 = Foo()
    foo2 = Foo()
    print id(foo1)
    print id(foo2)
    print isinstance(foo1, object)
    print isinstance(foo1, Foo)
    foo1.sayHi()
