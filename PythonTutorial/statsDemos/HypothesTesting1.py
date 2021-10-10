# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:50:14 2020

@author: Ankita Gogawale
"""

'''
Problem Statement
Consider the following independent samples s1 and s2:

s1 = [45, 38, 52, 48, 25, 39, 51, 46, 55, 46]
s2 = [34, 22, 15, 27, 37, 41, 24, 19, 26, 36]
The samples represent the life satisfaction score (computed through a methodology) 
of older adults and younger adults respectively.

Compute t-statistic for the above two groups, and display the t-score and p value in separate lines.

Hint: Use the ttest_ind function available in scipy.
'''


import numpy as np 
from scipy import  stats

s1=np.array([45, 38, 52, 48, 25, 39, 51, 46, 55, 46])
s2=np.array([34, 22, 15, 27, 37, 41, 24, 19, 26, 36])

t,p=stats.ttest_ind(s1,s2)
print(t)
print(p)