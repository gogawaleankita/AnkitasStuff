# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 18:50:05 2020

@author: Ankita Gogawale
"""

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import matplotlib

fig2= plt.figure(figsize=(8,8))
ds=gridspec.GridSpec(4,4)

plot1= plt.subplot(ds[0,1],title='plot1' )
plot1.set_xticks([]); plot1.set_yticks([])

plot2= plt.subplot(ds[1,1],title='plot2')
plot2.set_xticks([]); plot2.set_yticks([])

plot3= plt.subplot(ds[2,1],title='plot3')
plot3.set_xticks([]); plot3.set_yticks([])

plot4=plt.subplot(ds[0,2],title='plot4')
plot4.set_xticks([]); plot4.set_yticks([])

plot5=plt.subplot(ds[1,2],title='plot5')
plot5.set_xticks([]); plot5.set_yticks([])

plot6=plt.subplot(ds[2,2],title='plot6')
plot6.set_xticks([]); plot6.set_yticks([])



print(matplotlib.get_configdir()) 