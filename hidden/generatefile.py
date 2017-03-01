# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 21:41:46 2017

@author: Carmen
"""

f = open("fruits.txt", "w")

fruits = ["cherries", "grapes"]

import random
for i in range(20):
    fruit = random.choice(fruits)
    amount = random.randint(100, 999)
    f.write(str(fruit)+"\t"+str(amount)+"\n")
    
f.close()
