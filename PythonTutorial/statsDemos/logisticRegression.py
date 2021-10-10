# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:50:08 2020

@author: Ankita Gogawale
"""


import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd

iris = sm.datasets.get_rdataset("iris",cache=True).data 

iris_subset = iris[(iris.Species == "versicolor") | (iris.Species == "virginica")].copy()

print(iris_subset.Species.unique())


iris_subset.Species = iris_subset.Species.map({"versicolor": 1, "virginica": 0}) 

iris_subset.rename(columns={"Sepal.Length": "Sepal_Length", "Sepal.Width": "Sepal_Width",	"Petal.Length": "Petal_Length", 
                          "Petal.Width": "Petal_Width"}, inplace=True) 

model= smf.logit('Species ~ Petal_Length + Petal_Width', data=iris_subset).fit()

print(model.summary())

