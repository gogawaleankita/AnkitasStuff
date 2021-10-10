# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 23:29:41 2020

@author: Ankita Gogawale
"""



import pandas as pd
import numpy as np

from sklearn.datasets import load_boston

boston = load_boston()
dataset = pd.DataFrame(data=boston.data, columns=boston.feature_names)
dataset['target'] = boston.target
# dataset['test']=boston.test


X = dataset['RM']
Y = dataset['target']

import statsmodels.api as sm
import statsmodels.formula.api as smf


statsmodel= smf.ols('Y ~ X',data=dataset)
fittedModel=statsmodel.fit()

print(fittedModel.summary())
print(fittedModel.rsquared)