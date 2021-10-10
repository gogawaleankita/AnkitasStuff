# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 18:38:07 2020

@author: Ankita Gogawale



problem Statement  :
    
    
Question

The average number of bouquets sold by a flower shop is 10 per day. What is the probability that exactly 15 bouquets will be sold tomorrow?
Display the probability only(in decimal).
Hint:

Make use of poisson.pmf() function present in scipy.stats package.

"""

from scipy import stats
import numpy as np 

mu=10

actual_probability= stats.poisson.pmf(15,mu)
print(np.around(actual_probability))

