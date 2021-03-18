#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:36:25 2021

@author: Cesar A. Salgado E.

Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó $10, 
el segundo $20, el tercero $40 y así sucesivamente. Calcular cada pago mensual 
y el total de lo que pagó después de los 20 meses.

"""
pago = 10

for i in range(1,21):
    if(i == 1):
         print("Pago del mes",i,":\t",pago)
         continue
    
    pago *= 2
    print("Pago del mes",i,":\t",pago)
else:
    print("-----------------------------")
    print("Total del pago:\t", pago)