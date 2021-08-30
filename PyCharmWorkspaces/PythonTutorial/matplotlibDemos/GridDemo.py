# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:55:59 2020

@author: Ankita Gogawale
"""


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

def test_generate_figure1():
    t=np.arange(0.0, 5.0, 0.01)
    s1=np.sin(2*np.pi*t)
    s2=np.sin(4*np.pi*t)
    fig=plt.figure(figsize=(8,6))
    axes1=plt.subplot(2,1,1 ,title='Sin(2pix)')
    axes1.plot(t,s1)
    axes2= plt.subplot(2,1,2,title='Sin(4pix)')
    axes2.plot(t,s2)
    plt.show()
    

def test_generate_figure2():
    np.random.seed(1000)
    x=np.random.rand(10)
    y=np.random.rand(10)
    np.sqrt(x**2 +y**2)
    fig=plt.figure(figsize=(8,6))
    
    axes1=plt.subplot(2,2,1 ,title='Scatter plot with Upper Traingle Markers')    
    axes1.scatter(x,y,color='coral',marker='^',s=80)
    
    axes2=plt.subplot(2,2,2,title= 'Scatter plot with Plus Markers')
    axes2.set(xticks=(0.0, 0.4, 0.8, 1.2),yticks=(-0.2, 0.2, 0.6, 1.0 ))
    axes2.scatter(x,y,c='coral',s=80,marker='+')
    
    axes3=plt.subplot(2,2,3,title= 'Scatter plot with Circle Markers')
    axes3.set(xticks=(0.0, 0.4, 0.8, 1.2),yticks=(-0.2, 0.2, 0.6, 1.0 ))
    axes3.scatter(x,y,c='coral',s=80,marker='o')


    axes4=plt.subplot(2,2,4,title= 'Scatter plot with Diamond Markers')
    axes4.set(xticks=(0.0, 0.4, 0.8, 1.2),yticks=(-0.2, 0.2, 0.6, 1.0 ))
    axes4.scatter(x,y,color='z',s=80,marker='d')

    plt.show()
    
def test_generate_figure3():
    x=np.arange(1, 101)
    y1=x
    y2=x**2
    y3=x**3
    fig2= plt.figure(figsize=(8,6))
    ds=gridspec.GridSpec(2,2)
    axes1=plt.subplot(ds[0,0],title='y = x')
    axes2=plt.subplot(ds[1,0],title='y = x**2')
    axes3=plt.subplot(ds[0:,1],title='y = x**3')
    axes1.plot(x,y1)
    axes2.plot(x,y2)
    axes3.plot(x,y3)
    plt.tight_layout()
    plt.show()











    
    
    
test_generate_figure2()