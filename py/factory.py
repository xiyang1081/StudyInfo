#!/usr/bin/env python
#coding=utf-8

class Factory:
    def createFruit(self,fruit):
        if fruit=='apple':
            return Apple()
        elif fruit=='banana':
            return Banana()
class Fruit:
    def __str__(self):
        return 'Fruit'

class Apple(Fruit):
    def __str__(self):
        return 'Apple'

class Banana(Fruit):
    def __str__(self):
        return 'Banana'

if __name__=='__main__':
    f=Factory()
    print f.createFruit('banana')
