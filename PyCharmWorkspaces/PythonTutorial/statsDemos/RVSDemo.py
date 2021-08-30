# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:07:25 2020

@author: Ankita Gogawale

Problem Statement
Simulate a random experiment of tossing a coin 10000 times, and determine the count of Heads returned.

Hint: Define a binomial distribution with n = 1 and p = 0.5.

Use binom function from scipy.stats.
Set the random seed to 1.
Draw a sample of 10000 elements from a defined distribution. Assume that the values '0' and '1' 
represent Heads and Tails respectively.
Count the number of 'Heads' and display it. Make used of the 'bincount' method available in 'numpy'.



"""


import numpy as np
from scipy import stats




np.random.seed(1)
x= stats.binom.rvs(n=1,p=0.5,size=10000)
heads,tails=np.bincount(x)

print(heads)



