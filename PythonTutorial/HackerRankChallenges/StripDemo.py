#!/bin/python3

import sys
import os
import io
import re


# Complete the function below.

def main():
    zenPython = '''
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.pattern, givenList[i], re.M | re.I
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    '''

    fp = io.StringIO(zenPython)

    zenlines = fp.readlines()

    zenlines = [line.strip() for line in zenlines]

    portions = []

    pattern = r'[-*].*[-*]'
    portion = [re.search(pattern, i, re.M | re.I)  for i in zenlines ]
    portions=[]
    for i in portion:
        if i != None :
            str1=i.group().rstrip()
            str1= re.search(r'[a-zA-Z]+.*[a-zA-Z]+',str1, re.M | re.I)
            if  str1 != None :
                print(str1.group())
                portions.append(str1.group())

    return portions

# print(main())

addr = ['100 NORTH MAIN ROAD',
        '100 BROAD ROAD APT.',
        'SAROJINI DEVI ROAD',
        'BROAD AVENUE ROAD']

new_address=[]
for i in addr :
    if i.find(" ROAD") != -1 :

        i.replace(" ROAD"," RD")
        print(i)
        new_address.append(i)
print(new_address)


