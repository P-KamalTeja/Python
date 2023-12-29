# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:16:31 2020

@author: KAMAL TEJA
"""
i=1
a=1
while i<=100:
    if((a%3==0) | (a%5==0)):
        a=a+1
    else:
        print(a)
        a+=1
    i=i+1