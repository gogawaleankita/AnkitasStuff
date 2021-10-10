# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:49:33 2020

@author: Ankita Gogawale
"""


import statsmodels.api as sm
import pandas as pd
import statsmodels.formula.api as smf
import numpy as np
mtcars= sm.datasets.get_rdataset('mtcars')

data= pd.DataFrame(mtcars.data)

# print(data.columns)



linear_model1 = smf.ols('mpg ~ wt', data=data)

linear_model=linear_model1.fit()

# print(linear_model.pvalues)
print(np.round(linear_model.rsquared,3))
#print(linear_model.summary())








# import statsmodels.api as sm
# import numpy as np
# import pandas as pd
# import statsmodels.formula.api as smf
# from statsmodels.stats import anova

# mtcars = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data
# df = pd.DataFrame(mtcars)
# model = smf.ols(formula='np.log(mpg) ~ np.log(wt)', data=mtcars).fit()
# print(anova.anova_lm(model))
# print(anova.anova_lm(model).F["np.log(wt)"])
