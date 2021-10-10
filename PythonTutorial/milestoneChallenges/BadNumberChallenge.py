import math
import os
import sys
import random
import re


def goodSegment(badNumbers,l,r):
    badNumbers.sort()
    print(badNumbers)
    if(l!=badNumbers[0]):
        mylist=[[l,badNumbers[0]-1]]
    else:
        mylist = [[l, l]]
    longestseg=0
    for i in range(len(badNumbers)):
        if badNumbers[i]<=r :
            print((i,badNumbers[i]))
            if badNumbers[i]+1 == badNumbers[i+1]-1 :
                temp = [badNumbers[i] , badNumbers[i + 1]]
            else:
                temp= [badNumbers[i]+1,badNumbers[i+1]-1]

            print(temp)
            mylist.append(temp)
            if (longestseg >=0 and longestseg <=r):
                t1=abs(temp[1]+1-temp[0])
                if t1 >= longestseg:
                    longestseg=t1
        else:
            continue

    print(mylist)
    return longestseg

if __name__== '__main__':
    # fptr=open(os.environ['OUTPUT_PATH'],'w')
    # badNumbers_count=int(input().strip())
    badNumbers=[5,4,2,15]
    # for _ in range(badNumbers_count):
    #
    #     badNumbers_item=int(input().strip())
    #     badNumbers.append(badNumbers_item)
    # l=int(input().strip())
    # r=int(input().strip())
    l=1
    r=10
    result=goodSegment(badNumbers,l,r)
    print(result)