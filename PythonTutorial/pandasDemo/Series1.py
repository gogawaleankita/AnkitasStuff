# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:41:44 2020

@author: Ankita Gogawale
"""


import pandas as pd
import numpy as np



labels=['s1','s2','s3','s4','s5']
heights_A=pd.Series([176.2, 158.4, 167.6, 156.2,161.4],index=labels)
weights_A=pd.Series([85.1, 90.2, 76.8, 80.4, 78.9],index=labels)

df_A=pd.DataFrame({'Student_height ':heights_A,'Student_weight':weights_A})
#df_A.loc['s3'][0]='NaN'
#df_A.loc['s3'][1]='NaN'
df_A2= df_A.dropna()
print(df_A2)
df_A.to_csv('classA.csv', sep=',', encoding='utf-8')
# -
df_A2= pd.read_csv('classA.csv')
#print(df_A2)
df_A3= pd.read_csv('classA.csv',index_col= 0)
print(df_A3)

np.random.seed(100)

heights_B = pd.Series(np.random.normal(170.0,25.0,size=5),index=labels)
np.random.seed(100)
weights_B = pd.Series(np.random.normal(75.0,12.0,size=5),index=labels)

df_B= pd.DataFrame({'Student_height ':heights_B,'Student_weight': weights_B })


df_B.to_csv('classB.csv',index=0)
#m= pd.read_csv("classB.csv"); print(m)

df_B2=pd.read_csv('classB.csv')
print(df_B2)

df_B3=pd.read_csv('classB.csv',header=None)
print(df_B3)

df_B4=pd.read_csv('classB.csv',header=None,skiprows=2)
print(df_B4)
'''
peroid_rand=pd.date_range('11-Sep-2017', '17-Sep-2017',freq='M')
len(peroid_rand)
#             pd.period_range('11-Sep-2017', '17-Sep-2017', freq='M')          

d = pd.date_range('11-Sep-2017', '17-Sep-2017', freq='2D')
d=d+pd.Timedelta('1 days 2 hours')

#print(df_A.index.str.len())
g = df_A.groupby(df_A.index.str.len())
#print(g)
#print(g.filter(lambda x: len(x) > 1))
#print(df_A.loc[(df_A.r1 > 155) & (df.r2 < 189)])


np.random.seed(100)
columns=['A','B','C','D']
rows=['r1','r2','r3']

df=pd.DataFrame(np.random.randn(3,4),rows,columns)
print(df)
#print(df[lambda x : x.index.str.endswith('3')])

g = df.groupby(df.index.str.len())

print(g.aggregate({'A':len, 'B':np.sum}))
#print(df.iloc[:, lambda x : [0,]])


'''