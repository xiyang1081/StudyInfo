#!/usr/bin/env python
#coding=utf-8

class Fruit:
    price=0
    def __init__(self):
        self.__color='red'
    def getColor(self):
        print self.__color
    @classmethod
    def getPrice(self):
        print self.price
    def __getPrice(self):
        self.price=self.price+10
        print self.price

    count=classmethod(__getPrice)
class Apple(Fruit):
    pass

if __name__=='__main__':
    Fruit.getPrice()
    f=Fruit()
    f.getColor()
    Fruit.getPrice()
    Fruit.count()
    Fruit.getPrice()
    b=Fruit()
    Fruit.count()
    Fruit.getPrice()
    
