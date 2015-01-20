#!/usr/bin/env python
#coding=utf-8
#单例模式
方法一

 

import threading  
  
class Singleton(object):  
    __instance = None  
  
    __lock = threading.Lock()   # used to synchronize code  
  
    def __init__(self):  
        "disable the __init__ method"  
 
    @staticmethod  
    def getInstance():  
        if not Singleton.__instance:  
            Singleton.__lock.acquire()  
            if not Singleton.__instance:  
                Singleton.__instance = object.__new__(Singleton)  
                object.__init__(Singleton.__instance)  
            Singleton.__lock.release()  
        return Singleton.__instance  
 1.禁用__init__方法，不能直接创建对象。

 2.__instance，单例对象私有化。

 3.@staticmethod，静态方法，通过类名直接调用。

 4.__lock，代码锁。

 5.继承object类，通过调用object的__new__方法创建单例对象，然后调用object的__init__方法完整初始化。

 6.双重检查加锁，既可实现线程安全，又使性能不受很大影响。

 

方法二：使用decorator

 

#encoding=utf-8  
def singleton(cls):  
    instances = {}  
    def getInstance():  
        if cls not in instances:  
            instances[cls] = cls()  
        return instances[cls]  
    return getInstance  
 
@singleton  
class SingletonClass:  
    pass  
  
if __name__ == '__main__':  
    s = SingletonClass()  
    s2 = SingletonClass()  
    print s  
    print s2  
 

也应该加上线程安全

 

 

附：性能没有方法一高

 

import threading  
  
class Sing(object):  
    def __init__():  
        "disable the __init__ method"  
  
    __inst = None # make it so-called private  
  
    __lock = threading.Lock() # used to synchronize code  
 
    @staticmethod  
    def getInst():  
        Sing.__lock.acquire()  
        if not Sing.__inst:  
            Sing.__inst = object.__new__(Sing)  
            object.__init__(Sing.__inst)  
        Sing.__lock.release()  
        return Sing.__inst  
