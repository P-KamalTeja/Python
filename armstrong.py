# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:30:21 2020

@author: KAMAL TEJA
"""
def arm(n):
    result = 0
    temp = n
    while temp > 0:
        rem=temp%10
        result += rem**3
        temp//=10
    print(result)
    if result==n:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")
        
        
a=int(input("enter a number:"))
arm(a)


