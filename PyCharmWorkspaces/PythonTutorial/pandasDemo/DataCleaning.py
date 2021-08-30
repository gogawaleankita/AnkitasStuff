# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:18:54 2020

@author: Ankita Gogawale
"""


import pandas as pd
import numpy as np



labels=['s1','s2','s3','s4','s5']
heights_A=pd.Series([176.2, 158.4, 167.6, 156.2,161.4],index=labels)
weights_A=pd.Series([85.1, 90.2, 76.8, 80.4, 78.9],index=labels)

df_A=pd.DataFrame({'Student_height ':heights_A,'Student_weight':weights_A})
df_A.loc['s3'][0]='NaN'
df_A.loc['s3'][1]='NaN'
df_A2= df_A.dropna()
#print(df_A2)


mydict={'A':[1,2,np.nan],'B':[4,5,np.nan],'C':[np.nan,np.nan,np.nan]}
df=pd.DataFrame(mydict)
print(df)