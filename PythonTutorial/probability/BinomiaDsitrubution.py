# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 18:21:56 2020

@author: Ankita Gogawale




In each of 4 different competitions, Jin has 60% chance of winning. Assuming that the competitions are independent of each other, what is the probability that: Jin will win atleast 1 race,

Binomial Distribution Parameters

n=4

p=0.60

Display the probability in decimal.

Hint:

P(x>=1)=1-P(x=0)   

this means first  calculate will zero probability then subtrect from actual 
Use the binom.pmf() function of scipy.stats package to calculate the probability.
"""

from scipy import stats



n=4 
p=0.60

zero_P=stats.binom.pmf(0,n,p)

actual_P= 1- zero_P

print(actual_P)
