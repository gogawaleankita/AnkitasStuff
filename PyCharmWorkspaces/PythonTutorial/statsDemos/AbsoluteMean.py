# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:44:20 2020

@author: Ankita Gogawale
"""


import numpy as np
from scipy import stats

x= stats.norm(loc=32 ,scale=4.5)
np.random.seed(1)
sample= np.random.rand(100)
print(np.abs(sample.mean()-x.mean()))