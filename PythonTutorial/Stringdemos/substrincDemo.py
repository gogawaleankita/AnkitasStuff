#!/bin/python3

import sys
import os
import io
import re


# Complete the function below.
def subst(pattern, replace_str, string):
    mystring =string.replace(pattern, replace_str)
    return mystring
def main():
    addr = ['100 NORTH MAIN ROAD',
            '100 BROAD ROAD APT.',
            'SAROJINI DEVI ROAD',
            'BROAD AVENUE ROAD']
    new_address=[subst(" ROAD", " RD",i) for i in addr]
    return new_address

if __name__ == "__main__":
    print(main())


