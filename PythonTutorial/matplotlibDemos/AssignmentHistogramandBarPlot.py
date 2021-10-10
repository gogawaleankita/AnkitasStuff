# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:18:58 2020

@author: Ankita Gogawale





"""

from matplotlib import pyplot as plt
import numpy as np

def test_hist_of_a_sample_normal_distribution():
    fig= plt.figure(figsize=(8,6))
    ax=fig.add_subplot(111)
    ax.set(title='Histogram of a Single Dataset',ylabel='Bin Count',xlabel='X1')
    np.random.seed(100)
    x1= np.random.normal(loc=25,scale=3.0,size=1000)
    ax.hist(x1,bins=30,orientation='horizontal')
    plt.show()
    
def test_boxplot_of_four_normal_distribution():
    np.random.seed(100)
    with plt.style.context(['dark_background', 'seaborn-poster']):
        fig= plt.figure(figsize=(8,6))
        
        ax=fig.add_subplot(111)
        ax.set(title=' Box plot of Multiple Datasets',ylabel='Value',xlabel='Dataset')
    
        x1= np.random.normal(loc=25,scale=3.0,size=1000)
        x2=np.random.normal(loc=35,scale=5.0,size=1000)
        x3=np.random.normal(loc=55,scale=10.0,size=1000)
        x4=np.random.normal(loc=45,scale=3.0,size=1000)
        ax.boxplot([x1,x2,x3,x4],labels=['X1', 'X2', 'X3', 'X4'],notch=True,patch_artist=True)
        plt.show()

test_hist_of_a_sample_normal_distribution()
# test_boxplot_of_four_normal_distribution()