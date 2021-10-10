# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:05:32 2020

@author: Ankita Gogawale
"""

import numpy as np 
import pandas as pd 

np.random.seed(100)
inside=[1,2,3,1,2,3]
outside=['G1','G1','G1','G2','G2','G2']


heir_index= pd.MultiIndex.from_tuples(list(zip(outside,inside)))
df=pd.DataFrame(np.random.randn(6,2),heir_index,['A1','B1'])
df.index.names=['Groups','Num']
#print(df.loc['G1'].loc[2].loc['A1'])
print(df)


#print(df.xs('G1'))
print(df.xs(1,level='Num'))