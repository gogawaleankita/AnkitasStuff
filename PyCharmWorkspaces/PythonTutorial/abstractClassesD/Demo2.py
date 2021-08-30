# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:58:41 2020

@author: Ankita Gogawale
"""

from abc import ABC, abstractmethod

class A(ABC):

   # @classmethod
    @abstractmethod
    def m1(self):
        print('In class A, Method m1.')

class B(A):

   # @classmethod
    def m1(self):
        print('In class B, Method m1.')
    
    def m2():
        print('In class B, Method m2.')

b = B()
b.m1()
B.m2()

