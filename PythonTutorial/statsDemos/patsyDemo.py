# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:25:53 2020

@author: Ankita Gogawale
"""


# import numpy as np

# y = np.array([1, 2, 3, 4, 5])
# x1 = np.array([6, 7, 8, 9, 10])
# x2 = np.array([11, 12, 13, 14, 15])
# X = np.vstack([np.ones(5), x1, x2, x1*x2]).T

# print(y)
# print(X)


import patsy
import numpy as np

y = np.array([1, 2, 3, 4, 5])
x1 = np.array([6, 7, 8, 9, 10])
x2 = np.array([11, 12, 13, 14, 15])
data = {'y':y, 'x1':x1, 'x2':x2}

y, X = patsy.dmatrices('y ~ 1 + x1 + x2 + x1*x2', data)

print(y)
print(X)