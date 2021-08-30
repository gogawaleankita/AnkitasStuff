# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:32:28 2020

@author: admin
"""


import numpy as np
import statistics as stat


arr=np.array([9.2,10.7,6.8,9,3.4,5.7,5.7])

print(np.mean(arr))
print(np.median(arr))
print(stat.stdev(arr))
print(stat.variance(arr))
print(stat.mode(arr))

P_Seoul=1/4

P_Paris=1/4

P_Dubai=1/4

P_Switzerland=1/4

total_P= P_Seoul+P_Seoul+P_Dubai+P_Paris

print((P_Seoul+P_Switzerland)/total_P)