#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:12:18 2021

@author: Cesar A. Salgado E.

Program 01: Basic conditionals
"""

num = 10

if num >=0:
    print("Positive or zero")
else:
    print("Negative number:")
    
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("zero")
    else:
        print("positive number")
        
else:
    print("Negative number")


num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
    
    
            
