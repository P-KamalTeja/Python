# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:33:10 2020

@author: KAMAL TEJA
"""

from array import *

arr=array('i',[])
n=int(input("enter the length of array"))
for i in range(n):
        elm=int(input("enter the next value"))
        arr.append(elm)
    
val=int(input("enter the element to search"))
print(arr.index(val))