# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:45:55 2020

@author: Ankita Gogawale



John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .
"""


import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count=0
    for i in ar:
        for j in ar:
            if i==j:                
                print(i,"  ",j)
                
                break;
            
    print(count)

if __name__ == '__main__':
    
        
        ar = list([10,20,30,10,20,10])
        n=len(ar)
        result = sockMerchant(n, ar)

        print(str(result) + '\n')

   