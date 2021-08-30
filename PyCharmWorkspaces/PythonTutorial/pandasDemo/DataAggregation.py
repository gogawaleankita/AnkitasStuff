# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:21:11 2020

@author: Ankita Gogawale

statement :
    
    Task 1
Create a series named heights_A with values 176.2, 158.4, 167.6, 156.2, and 161.4. These values represent the heights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Create another series named weights_A with values 85.1, 90.2, 76.8, 80.4, and 78.9. These values represent the weights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Create a dataframe named df_A, which holds the height and weight of five students s1, s2, s3, s4 and s5.

Label the columns as Student_height and Student_weight, respectively.

Filter the rows from df_A, whose Student_height > 160.0 and Student_weight < 80.0, and capture them in another dataframe df_A_filter1.

Print the dataframe df_A_filter1.


newdf = df.iloc[[index for index,row in df.iterrows() if row['origin'] == 'JFK' and row['carrier'] == 'B6']]


"""


import pandas as pd
import numpy as np



labels=['s1','s2','s3','s4','s5']
heights_A=pd.Series([176.2, 158.4, 167.6, 156.2,161.4],index=labels)
weights_A=pd.Series([85.1, 90.2, 76.8, 80.4, 78.9],index=labels)
df_A=pd.DataFrame({'Student_height':heights_A,'Student_weight':weights_A})

df_A_filter1= df_A.loc[(df_A.Student_height> 160) &  (df_A.Student_weight < 80)]
df_A_filter1=df_A.query('Student_height>160 & Student_weight<80')
print(df_A_filter1)


df_A_filter2= df_A[lambda x : x.index.str.endswith('3')]
print(df_A_filter2)
df_A['Gender'] = ['M', 'F', 'M', 'M', 'F']

df_groups=df_A.groupby('Gender')
print(df_groups.mean())

