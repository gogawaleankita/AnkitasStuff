# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:08:28 2020

@author: Ankita Gogawale


Problem Statement
Perform the following tasks:

Load the R dataset Insurance from the MASS package.
Capture the data as a pandas dataframe.
Build a Poisson regression model with a log of an independent variable Holders, and dependent variable Claims.
Fit the model with data, and find the sum of the residuals.


https://vincentarelbundock.github.io/Rdatasets/doc/MASS/Insurance.html
"""


import statsmodels.api as sm
import  statsmodels.formula.api as smf 
import numpy as np
import pandas as pd 

data=pd.DataFrame(sm.datasets.get_rdataset("Insurance","MASS",cache=True).data)
model=smf.poisson('Claims ~ District + Group + Age + np.log(Holders)',data).fit()
print(np.sum(model.resid))
