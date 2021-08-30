# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:42:12 2020

@author: Ankita Gogawale
"""


import pandas as pd
import numpy as np



labels=['s1','s2','s3','s4','s5']
heights_A=pd.Series([176.2, 158.4, 167.6, 156.2,161.4],index=labels)
weights_A=pd.Series([85.1, 90.2, 76.8, 80.4, 78.9],index=labels)

df_A=pd.DataFrame({'Student_height':heights_A,'Student_weight':weights_A})



gender= ['M', 'F', 'M', 'M', 'F']
df_A['Gender']=gender
s= pd.Series([165.4, 82.7, 'F'], index=['Student_height', 'Student_weight', 'Gender'],name='s6')
#s= pd.Series(data=dict(zip(['Student_height', 'Student_weight', 'Gender'],[165.4, 82.7, 'F'])),name='s6')
df_A=df_A.append(s,ignore_index=False)
df_AA=df_A
print((df_AA))

np.random.seed(100)
heights_B=pd.Series( np.random.normal(170.0,25.0,size=5),index=labels)
np.random.seed(100  )
weights_B= pd.Series(np.random.normal(75.0,12.0,size=5),index=labels)
df_B=pd.DataFrame({'Student_height':heights_B,'Student_weight':weights_B})
df_B.index=[ 's7', 's8', 's9', 's10', 's11']
gender=['F', 'M', 'F', 'F', 'M']
df_B['Gender']=gender
df=pd.concat([df_AA,df_B])
print(df)
