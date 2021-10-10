# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:04:08 2020
statement : 
    
    The teacher wants a group to be formed for the upcoming dance competition. She wants a group of 5 dancers consisting of 3 boys and 2 girls. In how many ways can a group of 5 dancers be formed by selecting 3 boys out of 6 and 2 girls out of 5 ? Help her out!

Display the number of ways a group of 5 dancers consisting of 3 boys and 2 girls can be formed
@author: admin
"""
import math
import numpy as np
import itertools as itr
no_of_boys=6
no_of_girls=5
required_girls=2
required_boys=3
required=math.fsum([required_boys+required_girls])
total =math.fsum([no_of_boys,no_of_girls])
select_girls= math.factorial(no_of_girls)/(math.factorial(no_of_girls-required_girls)*(math.factorial(required_girls)))
select_boys= math.factorial(no_of_boys)/(math.factorial(no_of_boys-required_boys)*(math.factorial(required_boys)))
#required_people= math.factorial(total)/(math.factorial(total-required)*math.factorial(required))
dance_group=(select_boys*select_girls)

print(dance_group)
