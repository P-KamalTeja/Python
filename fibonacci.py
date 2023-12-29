# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:30:30 2020

@author: KAMAL TEJA
"""


def fib(n):
    if n < 0:
        print("enter number greater than zero")
    else:
        a = -1
        b = 1
        for i in range(n + 1):
            a, b = b, a + b
            print(b)


fib(5)
