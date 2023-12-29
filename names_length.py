# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:17:12 2020

@author: KAMAL TEJA
"""

def users(lst):
    count=0
    for i in range(len(lst)):
        if(int(len(lst[i]))>=5):
            count +=1
            print("{} user(s) are having their name less than length of 5 ".format(count))
    else:
        print("all users name are less than length of 5")
            
a=int(input("enter the no.of users:"))
b=[]
for i in range(a):
    c=input("enter the {} user name:-".format(i))
    b.append(c)

users(b)