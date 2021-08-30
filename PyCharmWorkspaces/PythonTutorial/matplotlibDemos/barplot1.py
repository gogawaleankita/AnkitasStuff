# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 23:50:36 2020



	petal_len = [1.46, 4.26, 5.55]
	petal_wd = [0.24, 1.33, 2.03]
	species = ['setosa', 'versicolor', 'viriginica']
	
	species_index2=[0.9, 1.9, 2.9]
    species_index3=[1.1, 2.1, 3.1]
    species_index4=[1.3, 2.3, 3.3]







@author: Ankita Gogawale
"""
from matplotlib import  pyplot as plt 
import numpy as np



fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(211)
ax.set(title='Avg. Quarterly Sales',
      xlabel='Quarter', ylabel='Sales (in millions)')
quarters = [1, 2, 3]
sales_2017 = [25782, 35783, 36133]
ax.bar(quarters, sales_2017,width=0.6, edgecolor='yellow')
ax.set_xticks(quarters)
ax.set_xticklabels(['Q1-2017', 'Q2-2017', 'Q3-2017'])
# plt.show()


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set(title='Avg. Quarterly Sales',
      xlabel='Quarter', ylabel='Sales (in millions)')
quarters = [1, 2, 3]
x1_index = [0.8, 1.8, 2.8]; x2_index = [1.2, 2.2, 3.2]
sales_2016 = [28831, 30762, 32178]; sales_2017 = [25782, 35783, 36133]
ax.bar(x1_index, sales_2016, color='yellow', width=-0.4, edgecolor='black', label='2016')
ax.bar(x2_index, sales_2017, color='red', width=0.4, edgecolor='black', label='2017')
ax.set_xticks(quarters)
ax.set_xticklabels(['Q1', 'Q2', 'Q3'])
ax.legend()
plt.show()  