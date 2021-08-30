# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 20:38:29 2020

@author: Ankita Gogawale

statement : 
    Create the following two Series: nameid = pd.Series(range(101, 111))

name = pd.Series(['person' + str(i) for i in range(1, 11)])
 
Create the dataframe master with series nameid and name. Let the column names be nameid and name respectively.

Create the dataframe transaction using the command: transaction = pd.DataFrame({'nameid':[108, 108, 108,103], 'product':['iPhone', 'Nokia', 'Micromax', 'Vivo']})

Merge master with transaction on nameid, and save the merged dataframe as mdf. Perform inner join. Note: Use the merge method.

Display mdf.
"""


import pandas as pd 
import numpy as np 

nameid = pd.Series(range(101, 111))
name = pd.Series(['person' + str(i) for i in range(1, 11)])
master = pd.DataFrame()
master['nameid'] = nameid
master['name'] = name

transaction = pd.DataFrame({'nameid':[108, 108, 108,103], 'product':['iPhone', 'Nokia', 'Micromax', 'Vivo']})

mdf = pd.merge(master,transaction,on='nameid')
print(mdf)


dates = pd.date_range('1-Sep-2017', '15-Sep-2017')
##print(dates[2])
datelist = ['14-Sep-2017', '9-Sep-2017']
dates_to_be_searched= pd.to_datetime(datelist)
#print(dates_to_be_searched)
#print(dates_to_be_searched.isin(dates))
arraylist = [['classA']*5 + ['classB']*5, ['s1', 's2', 's3','s4', 's5']*2] 
mi_index = pd.MultiIndex.from_arrays(arraylist)
#print(mi_index.levels)