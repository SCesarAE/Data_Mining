#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 18:14:06 2021

@author: Cesar A. Salgado E.

Solicitar n números enteros y decir cuántos son pares, cuántos impares, cuántos 
negativos, cuantos positivos y cuántos ceros
"""

n= int(input("Enter the quantity of numbers: "))

for i in range(n):
    num = int(input(f"Enter the {i+1}º: "))
    
    if num > 0:
        print("Is a positive number")
    elif num < 0:
        print("Is a negative number")
    else:
        print("It's Zero")