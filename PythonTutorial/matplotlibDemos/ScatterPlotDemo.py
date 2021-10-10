# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:56:01 2020

@author: Ankita Gogawale
"""


from matplotlib import  pyplot as plt 
import numpy as np


def test_sine_wave_plot():
    t= np.linspace(0.0,20.0,200)
    v=np.sin(2.5*np.pi*t)
    fig= plt.figure(figsize=(12,3))
    ax=fig.add_subplot()
    ax.set(title='Sine Wave',ylabel='Voltage (mV)',xlabel='Time (seconds)',
           xlim=[0,2],ylim=[-1,1],yticks=(-1,0,1))
    ax.set_xticks((0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0))
    plt.grid(b=True, which='both', color='0.65', linestyle='--')
    ax.plot(t,v ,color='red',label='sin(t)')
    plt.legend()
    plt.show()
    
def test_multi_curve_plot():
    fig=plt.figure(figsize=(12,3))
    ax=fig.add_subplot()
    x= np.linspace(0.0,5.0,20)
    y1 = x;y2 = x**2;y3 = x**3
    ax.set(title='Linear, Quadratic, & Cubic Equations',xlabel='X',ylabel='f(X)')
    plt.plot(x,y1,label='y = x',color='red', marker='o')
    plt.plot(x,y2,label='y = x**2',color='green', marker='s')
    plt.plot(x,y3,label='y = x**3',color='blue',marker='^')
    plt.legend()
    plt.show()

def test_scatter_plot():
    fig=plt.figure(figsize=(12,3))
    ax=fig.add_subplot()
    s = [50, 60, 55, 50, 70, 65, 75, 65, 80, 90, 93, 95]
    months=['Jan', 'Feb','Mar', 'Apr','May', 'Jun','Jul','Aug','Sep', 'Oct','Nov','Dec']
    month=np.arange(1,13)
    ax.set(title="Cars Sold by Company 'X' in 2017",xlim=[0,13],ylim=[20,100],
           xlabel='Months',ylabel='No. of Cars Sold',
           xticks=(1, 3, 5, 7, 9,  11),
          
           )
    plt.scatter(months,s,color='red')
    
    plt.show()


test_sine_wave_plot()
test_multi_curve_plot()
test_scatter_plot()   

    