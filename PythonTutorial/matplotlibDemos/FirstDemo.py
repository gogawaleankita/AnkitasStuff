# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 19:18:01 2020

@author: Ankita Gogawale
"""


from matplotlib import pyplot as plt 

fig = plt.figure(figsize=(8,6))
ax=fig.add_subplot(211)

days = [1, 5, 8, 12, 15, 19, 22, 26, 29]
temp = [29.3, 30.1, 30.4, 50, 32.3, 100, 31.8, 124, 300]


t=[1,2,3,4,5]
d=[52,101,115,200,205]
ax.set(title='Time vs Distance Covered' , xlabel='time (seconds)',
       ylabel='distance (meters)',xlim=[0,max(days)+5],ylim=[0,max(temp)+50])


plt.plot(days,temp ,label='days~temp',color='navy',linewidth=2,linestyle='-',marker='o')
plt.legend()
ax.scatter(t,d,label='d~t',color='red',marker='T',edgecolors='black')
plt.show()