# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:34:40 2020

@author: Ankita Gogawale
"""


def findMiddleQuartile(datalist):
    middleQuartile=0
    limit=round(len(datalist)/2)
    if len(datalist)%2==1:
        
        middleQuartile=datalist[limit]       
    else:        
        middleQuartile=round((datalist[limit]+datalist[ limit-1])/2,1)
    
    return middleQuartile



mydict={
        {
          'data':'6 12 8 10 20 16'
              ,'freqency':'5 4 3 2 1 5'
        
        },
            {
          'data':'6 12 8 10 20 16'
              ,'freqency':'5 6 7 8 9 10'
        
        },
        {
          'data':'10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10 20 10 40 30 50 20 10 40 30 50'
              ,'freqency':'1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20'
        
        },
        {
          'data':'10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10'
              ,'freqency':'1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20'
        
        },
        {
          'data':'10 40 30 50 20 10 40 30 50 20'
        ,'freqency':'1 2 3 4 5 6 7 8 9 10'
        
        },
        {
          'data':'10 40 30 50 20'
        ,'freqency':'1 2 3 4 5'
        
        }
        
        }



print()

n=6
data='10 40 30 50 20'
frequency='1 2 3 4 5'
datalist=[ int(i) for i in data.split(' ')]
frequencylist=[int(i) for i in frequency.split(' ')]
finaldatalist=[]
k=0
for i in frequencylist:   
    for j in range(i):
        finaldatalist.append(datalist[k])
    k=k+1

finaldatalist.sort()
limit=round(len(finaldatalist)/2)
firstQuartile=findMiddleQuartile(finaldatalist[0:limit])
middleQuartile=findMiddleQuartile(finaldatalist)

thirdQuartile=0
if len(finaldatalist)%2==0:
    thirdQuartile=findMiddleQuartile(finaldatalist[limit:])
else:
    
    thirdQuartile=findMiddleQuartile(finaldatalist[limit-1:])

 
print(abs(thirdQuartile-firstQuartile))



# 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30,30
# 30
# 30, 30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50


