# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:04:11 2020

@author: Ankita Gogawale
"""


import numpy as np 
from scipy import stats 

s = np.array([26, 15, 8, 44, 26, 13, 38, 24, 17, 29])
print(stats.mode(s))
'''
print(np.mean(s) )
print(np.median(s))

print(np.percentile(s,[25,75],interpolation='lower'))
print(stats.iqr(s,rng=(25,75),interpolation='lower'))
print(stats.skew(s))
print(stats.kurtosis(s))
'''


#print(np.random.choice([11, 22, 33], 2, replace=True))

x = stats.norm(loc=1.0, scale=2.5)

print(x)

print(x.pdf([-1, 0, 1]))

print(x.cdf([-1, 0, 1]))

print(x.rvs((2,3)))
