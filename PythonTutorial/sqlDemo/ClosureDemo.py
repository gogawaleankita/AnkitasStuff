# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:55:18 2020

@author: Ankita Gogawale
"""


def factory(n):
    def current():
        return n
    def counter():
        return n+1
    mylist= list([current,counter])
    return mylist
    
f_current, f_counter = factory(2)


func_lst = [f_current, f_counter]
res_lst = list()
for func in func_lst:
    res_lst.append(func())
    
print(res_lst)


def bind(func):
    func.data = 9
    return func

@bind
def add(x, y):
    return x + y

print(add(3, 10))
print(add.data)