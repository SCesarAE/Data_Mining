#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 18:33:50 2021

@author: Cesar A. Salgado E.

Escribir un programa que imprima los números pares entre 1 y un número entero 
dado por el usuario

"""

num = int(input("Enter the number: "))

for i in range(1, num+1):
    if(i % 2 == 0):
        print (i)