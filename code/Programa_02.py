#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:28:35 2021

@author: Cesar A. Salgado E.

Program 03: Basic For
"""

for i in range(11):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1, 11, 2):
    print(i)

#Use break
for i in range(10):
    if i == 3:
        break
    print(i)
print("Fin")

#Use continue
for i in range(10):
    if i ==3 or i == 5:
        continue
    print(i)
print("Fin")

#Use of else in for
for i in range(10):
    if i ==3:
        break
    print(i)
else:#este else pertenece al for
    print("no numbers Left.")
    
#Nested fors
for i in range(1,11):
    for j in range(1,11):
        k = i * j
        print(i,'*',j,'=',k)
    print('hola')