# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 18:20:06 2020

@author: Ankita Gogawale


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.testing.decorators import image_comparison

@image_comparison(baseline_images=['Iris_Sepal_Length_BarPlot'],extensions=['png'])
def test_barplot_of_iris_sepal_length():

    # Write your functionality below


@image_comparison(baseline_images=['Iris_Measurements_BarPlot'],extensions=['png'])
def test_barplot_of_iris_measurements():

    # Write your functionality below


@image_comparison(baseline_images=['Iris_Petal_Length_BarPlot'],extensions=['png'])
def test_hbarplot_of_iris_petal_length():

    # Write your functionality below
"""



import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.testing.decorators import image_comparison


def test_barplot_of_iris_sepal_length():
    fig=plt.figure(figsize=(8,6))
    ax=fig.add_subplot(111)
    species=['setosa', 'versicolor', 'viriginica']
    index= [0.2, 1.2, 2.2] 
    sepal_len=[5.01, 5.94, 6.59]
    ax.set(title='Mean Sepal Length of Iris Species',xlabel='Species',
           ylabel='Sepal Length (cm)',
           xlim=[0,3],ylim=[0,7],xticks=( 0.45, 1.45,  2.45)
           )
    plt.bar(species,sepal_len)
    plt.show()
    
def test_barplot_of_iris_measurements():
	
    fig=plt.figure(figsize=(8,6))
    ax=fig.add_subplot(111)
    sepal_len = [5.01, 5.94, 6.59]
    sepal_wd = [3.42, 2.77, 2.97]
    petal_len = [1.46, 4.26, 5.55]
    petal_wd = [0.24, 1.33, 2.03]
    species = ['setosa', 'versicolor', 'viriginica']
    species_index1=[0.7, 1.7, 2.7]
    species_index2=[0.9, 1.9, 2.9]
    species_index3=[1.1, 2.1, 3.1]
    species_index4=[1.3, 2.3, 3.3]	
    ax.set(title='Mean Sepal Length of Iris Species',xlabel='Species',
           ylabel='Sepal Length (cm)',xticks=(1.1,2.1,3.1),
           xlim=[0,3],ylim=[0,7]
           )
    
    ax.bar(species_index1,sepal_len,color='c',width=0.2,edgecolor='black',tick_label =species)
    ax.bar(species_index2,sepal_wd,color='m',width=0.2,edgecolor='black',tick_label =species)
    ax.bar(species_index3,petal_len,color='y',width=0.2,edgecolor='black',tick_label =species)
    ax.bar(species_index4,petal_wd,color='orange',width=0.2,edgecolor='black',tick_label =species)
    plt.show()

def test_hbarplot_of_iris_petal_length():
    fig=plt.figure(figsize=(12,5))
    ax=fig.add_subplot(111)
    species=['setosa', 'versicolor', 'viriginica']
    index = [0.2, 1.2, 2.2]
    petal_len = [1.46, 4.26, 5.55]
    ax.set(title='Mean Petal Length of Iris Species',xlabel='Petal Length (cm)',
           ylabel='Species',
           xlim=[0,3],ylim=[0,7]
           )
    ax.barh(index,petal_len, height=0.5, color='c',edgecolor='black')
    ax.set_yticks([0.45,1.45,2.45])
    ax.set_yticklabels(species)
    plt.show()
    
test_hbarplot_of_iris_petal_length()



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    