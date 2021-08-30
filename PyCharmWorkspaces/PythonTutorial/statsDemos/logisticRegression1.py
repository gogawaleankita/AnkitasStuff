# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:23:22 2020

@author: Ankita Gogawale


Problem Statement
Perform the following tasks:

Load the R dataset biopsy from the MASS package.
Capture the data as a pandas dataframe.
Rename the column name class to Class.
Transform the Class column values benign and malignant to '0' and '1' respectively.
Build a logistic regression model with independent variable V1 and
 dependent variable Class.
Fit the model with data, and display the pseudo R-squared value
"""

import numpy as np
import pandas as pd 
import statsmodels.api as sm
import statsmodels.formula.api as smf 


data = pd.DataFrame(sm.datasets.get_rdataset('biopsy','MASS').data)
data = data.rename(columns={'class':'Class'})
data.Class= data.Class.map({'benign':0,'malignant':1})

model= smf.logit('Class ~  V1 ',data).fit()

print(model.prsquared)


