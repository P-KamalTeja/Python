# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:32:58 2020

@author: KAMAL TEJA
"""

def fact(n):
    if(n<0):
        print("enter the number greater than zero")
    else:
        fact=1
        for i in range (1,n+1):
            fact *= i
        return fact
x=int(input("Enter the number to get its factorial:-"))
result=fact(x)
print(result)