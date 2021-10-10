# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:04:31 2020

@author: Ankita Gogawale
"""


import statsmodels.api as sm 
import statsmodels.formula.api as smf 
import pandas as pd 
import numpy as np 
from statsmodels.stats  import anova

data=pd.DataFrame( sm.datasets.get_rdataset('mtcars') .data  )
model1= smf.ols('mpg ~ wt ',data).fit()
anvova=anova.anova_lm(model1)
print(anvova.F["wt"])


model2=smf.ols('np.log(mpg) ~ np.log(wt)', data).fit()
print(anova.anova_lm(model2).F['np.log(wt)'])
