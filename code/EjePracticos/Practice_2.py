#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:58:53 2021

@author: Cesar A. Salgado E.


Una persona empieza a ahorrar 2 centavos el 1 de enero, 4 centavos el 2 de 
enero, 8 centavos el 3, 16 el 4 y así sucesivamente hasta el 31 de diciembre. 
Calcular cuánto habrá ahorrado en PESOS al final del año (año no bisiesto).
"""

ahorro = 1

for i in range(1,365):
    ahorro *= 2
    
else:
    print("Ahorro al final del año: $", ahorro/100)