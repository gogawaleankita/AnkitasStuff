# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:29:49 2020

@author: Ankita Gogawale
"""


def star(func):
    print("inside star",func.__name__)
    def inner(args, **kwargs): 
        print("" * 3)
        func(args, **kwargs)
        print("" * 3) 
    return inner

def percent(func):
    print("inside percent ",func.__name__)
    def inner(*args, **kwargs):
        print("%" * 3)
        func(*args, **kwargs)
        print("%" * 3); 
    return inner

@star
@percent
def printer(msg): 
     print(msg)
printer("Hello")