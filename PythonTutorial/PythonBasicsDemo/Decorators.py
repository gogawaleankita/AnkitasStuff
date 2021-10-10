# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:12:46 2020

@author: Ankita Gogawale
"""


def outer(func):

    def inner():
        print("Accessing :", 
                  func.__name__)
        return func("Ankita")
    return inner



def outerGreetings(func):
    def inner():
        print("inside OuterF\Greetings : ",func.__name__)
        return func()
    return inner


@outerGreetings
def greet():
   print('Hello!')



def getName(name):
    print ("values  "+name)


greet()

wish=outer(getName)
wish()