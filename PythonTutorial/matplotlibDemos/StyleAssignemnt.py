# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:03:46 2020

@author: Ankita Gogawale
    
"""


import matplotlib.pyplot as plt

def generateGraph(styletext):
    sepal_len = [5.01, 5.94, 6.59]
    petal_len = [1.46, 4.26, 5.55]
    petal_wd = [0.24, 1.33, 2.03]
    sepal_wd = [3.42, 2.77, 2.97]
    species = ['setosa', 'versicolor', 'viriginica']
    species_index1 = [0.7, 1.7, 2.7]
    species_index2 = [0.9, 1.9, 2.9]
    species_index3 = [1.1, 2.1, 3.1]
    species_index4 = [1.3, 2.3, 3.3]
    
    with plt.style.context(styletext):
        fig=plt.figure(figsize=(8,6))
        ax=fig.add_subplot(111)
        ax.set(title='Mean Measurements of Iris Species',xlabel='Species'
               ,ylabel='Iris Measurements (cm)',xlim=[0.5,3.7]
               ,ylim=[0,10],xticks=(1.1,2.1,3.1)
               )
        ax.bar(species_index1,sepal_len,width=0.2,label='sepal Length',tick_label =species)
        ax.bar(species_index2,sepal_wd,width=0.2,label='sepal Length',tick_label =species)
        ax.bar(species_index3,petal_len,width=0.2,label='sepal Length',tick_label =species)
        ax.bar(species_index4,petal_wd,width=0.2,label='sepal Length',tick_label =species)
        ax.legend()
        plt.show()

def test_generate_plot_with_style1():
    generateGraph('ggplot')

def test_generate_plot_with_style2():
    generateGraph('seaborn-colorblind')
    

def test_generate_plot_with_style3():
    generateGraph('grayscale')

test_generate_plot_with_style3()