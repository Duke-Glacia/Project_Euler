#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def Fibonnachi(n):
    x=[]
    for i in range(n):
        x.append(F(i))
    return x
    
    
i=1
while F(i)<4000000:
    i+=1
    print (F(i))
    print (i)
    
    
x = list(map(int, x))  
    


    
