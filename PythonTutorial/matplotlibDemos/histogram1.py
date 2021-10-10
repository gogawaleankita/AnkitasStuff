# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:40:43 2020

@author: Ankita Gogawale
"""


from matplotlib import pyplot as plt 
import numpy as np 

x= 60 + np.round( 10* np.random.randn(1000))
fig= plt.figure(figsize=(8,6))
ax=fig.add_subplot(111)
ax.hist(x,color='pink',bins=11,normed=True,w)
plt.show()


