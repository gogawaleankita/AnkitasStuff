# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:36:04 2020

@author: Ankita Gogawale
"""




n=int(input())
data='10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10'
datalist=[ int(i) for i in data.split(' ')]
weight='1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20'
weightlist=[ int(i) for i in weight.split(' ')]

# sumofdata_weight= np.array(datalist)* np.array(weightlist)
# print(sumofdata_weight.sum()/np.array(weightlist).sum())

sumofdata_weight=0
for i in range(n):
    sumofdata_weight  += datalist[i]*weightlist[i]
    
print(round(sumofdata_weight/sum(weightlist),1))