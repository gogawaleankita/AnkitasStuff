# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:34:30 2020

@author: Ankita Gogawale
"""


from sklearn.datasets import load_boston
import pandas as pd
boston = load_boston()
dataset = pd.DataFrame(data=boston.data, columns=boston.feature_names)
dataset['target'] = boston.target



X=dataset.drop('target',axis=1)
Y=dataset['target']


# print(X.corr())
print(X['NOX'].corr(X['DIS']))

import statsmodels.api as sm

Xc=sm.add_constant(X)

model=sm.OLS(Y,Xc).fit()
print(model.summary())
print(model.rsquared)