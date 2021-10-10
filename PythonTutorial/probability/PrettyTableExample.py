# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 18:47:42 2020

@author: Ankita Gogawale
"""


from  prettytable  import PrettyTable
import numpy as np
from scipy import stats
t = PrettyTable(['Marital Status','Middle school', 'High School','Bachelor','Masters','PhD'])
t.add_row(['Single',18,36,21,9,6])
t.add_row(['Married',12,36,45,36,21])
t.add_row(['Divorced',6,9,9,3,3])
t.add_row(['Widowed',3,9,9,6,3])
# print (t)

arr=np.array([[18,36,21,9,6],[12,36,45,36,21],[6,9,9,3,3],[3,9,9,6,3]])
# print(arr)

stat,p_value,dof,expected = stats.chi2_contingency(arr)
p=0.05
print(stat)
print(dof)
print(p_value)

if p_value < p:
    print("Reject the Null Hypothesis")
else:
    print("Failed to reject the Null Hypothesis")











