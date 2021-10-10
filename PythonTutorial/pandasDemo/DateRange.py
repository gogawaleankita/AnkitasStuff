# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:39:37 2020

@author: Ankita Gogawale

create an index named dates representing a range of dates starting from 1-Sep-2017 to 15-Sep-2017.
Note: Use the date_range method of pandas.

Print the 3rd element of the created DateTimeIndex.
"""


import pandas as pd
import numpy as np 

dates= pd.date_range('1-sep-2017','15-sep-2017')
print(dates[2])



np.random.seed(100)
inside=[1,2,3,1,2,3]
outside=['G1','G1','G1','G2','G2','G2']
heir_index= pd.MultiIndex.from_tuples(list(zip(outside,inside)))
df=pd.DataFrame(np.random.randn(6,2),heir_index,['A1','B1'])
#print(df.loc['G1'].loc[2].loc['A1'])
#print(df)


print(df.xs('G1'))