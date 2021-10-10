# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:52:31 2020

@author: Ankita Gogawale
"""

import math


n=input()
data='10 40 30 50 20'
datalist=[int(i) for i in data.split(' ')]
mean = round(sum(datalist)/n,1)
sumofSquare=0
for i in datalist:
    sumofSquare += (i-mean)**2

stdDeviation= round(math.sqrt(  sumofSquare/n),1)

print(stdDeviation)
    