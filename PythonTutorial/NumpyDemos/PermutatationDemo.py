# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 12:40:32 2020

@author: Ankita 
"""


import numpy as np
import itertools as itr

arr=np.array(['A','B','C','D'])
arr1= list(itr.permutations(arr,2))
for i in arr1:
    print(i)

arr2= list( itr.combinations(arr, 2))
for i in arr2:
    print(i)
    
print(len(arr1))
print(len(arr2))
