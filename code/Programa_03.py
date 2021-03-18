#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:17:00 2021

@author: Cesar Antonio Salgado Escoto

Program 03= Basic While
"""

n = 10
suma = 0 #acumulador
i = 0 #counter

while i < n:
    i = i +1 #count
    suma += i #acumulate

print('The sum is', suma)


#Use of break
n = 10
suma = 0
i = 0

#use of break
while i < n:
    i = i +1
    if i == 3:
        break
    suma += i
print('The sum is ', suma)


#use of continue
n = 10
suma = 0
i = 0

while i < n:
    i = i +1
    if i == 3:
        continue
    suma += i
print('The sum is ', suma)


#use of else
n = 10
suma = 0
i = 0
while i < n:
    i = i +1
    if i == 3:
        break
    suma += i
    print(i, suma)
else:
    print('The sum is ',suma)
    
    
    
    
    
    
    
    
    
    
    
    
    
    