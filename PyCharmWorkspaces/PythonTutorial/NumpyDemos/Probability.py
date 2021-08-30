# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 14:17:58 2020

@author: Ankita 



On New Year's Eve, the probability of a person having a car accident is 0.09. 
The probability of a person driving while intoxicated is 0.32
 and probability of a person having a car accident while
 intoxicated is 0.15. What is the probability of a person driving while intoxicated or having a car accident?

P(accident)=0.09

P(intoxicated)=0.32

P(accident and intoxicated)=0.15

Display the probability in decimal.

Hint:

Use Addition rule
Non-Mutually Exclusive
"""


p_accident=0.09
p_intoxicted=0.32
p_intoxicated_accident=0.15


p= p_accident+p_intoxicted-p_intoxicated_accident
print(p)

