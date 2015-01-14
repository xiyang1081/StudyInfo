#!/usr/bin/env python
#coding=utf-8

class Fruit:
    price=0
    def __init__(self):
        self.__color='red'
    def getColor(self):
        print self.__color
    @staticmethod
    def getPrice():
        print Fruit.price
    def __getPrice():
        Fruit.price=Fruit.price+10
        print Fruit.price

    count=staticmethod(__getPrice)
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
    
