# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:21:41 2020

@author: Ankita Gogawale
"""


import os
import re
import random 
import sys
import requests
from requests.exceptions import HTTPError
import json
def avgRotorSpeed(statusQuery, parentId):
    pageNumber=1
    datas=[]
    data=[]   
    try:  
         while(pageNumber<=4):
             
             url= "https://jsonmock.hackerrank.com/api/iot_devices/search?status={}&page={}".format(statusQuery,pageNumber)
             pageNumber= pageNumber+1
             response=requests.get(url)
             data=json.loads(response.text)
             #print((data['data'][]))
             datas.append(data['data']) 
    except : 
        print("Error while loading Data")
    
    #data=[]
    d=[]
    for i in datas :
        for  j in  i:
            if 'parent' in j.keys() :
                if j['parent']!=None and j['parent']['id']==parentId:  
                    d.append( j['operatingParams']['rotorSpeed'])
                
            
            
    try :
        avgResult=int(sum(d)/len(d))
    except: 
            avgResult=0
        
    return avgResult
        # Write your code here

if __name__ == '__main__':
    statusQuery = "RUNNING"
   
    parentId = int(7)

    result = avgRotorSpeed(statusQuery, parentId)

    print(str(result) + '\n')

  
