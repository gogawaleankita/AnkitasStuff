# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:48:31 2020

@author: Ankita Gogawale
"""


from matplotlib import pyplot as plt 
import  numpy as np


np.random.seed(100)
x = 50 + 10*np.random.randn(1000)
y = 70 + 25*np.random.randn(1000)
z = 30 + 5*np.random.randn(1000)
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set(title="Box plot of Student's Percentage",
      xlabel='Class', ylabel='Percentage')
ax.boxplot([x, y, z], labels=['A', 'B', 'C'], vert=False,notch=True, bootstrap=10000)
plt.show()