# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:03:03 2020

@author: Ankita Gogawale
"""

def findMiddleQuartile(datalist):
    middleQuartile=0
    limit=round(len(datalist)/2)
    if len(datalist)%2==1:
        
        middleQuartile=datalist[limit]       
    else:        
        middleQuartile=round((datalist[limit]+datalist[ limit-1])/2)
    
    return middleQuartile


data='3 7 8 5 12 14 21 15 18 14'
data='3 7 8 5 12 14 21 13 18'
datalist=[ int(i) for i in data.split(' ')]
datalist.sort()

limit=round(len(datalist)/2)
print(findMiddleQuartile(datalist[0:limit]))
print(findMiddleQuartile(datalist))
if len(datalist)%2==0:
    print(findMiddleQuartile(datalist[limit:]))
else:
    print(findMiddleQuartile(datalist[limit+1:]))
   






    
        
    
