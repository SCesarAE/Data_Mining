#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:55:50 2021

@author: Cesar A. Salgado E.

Files and general usege of pandas
"""

import matplotlib.pyplot as plt
import pandas as pd

w_d = 'home/chicho/Documents/Universidad/Mineria de Datos/DM/data/'
f_i = w_d + 'info_estudiantes.csv'

with open(f_i, 'r', encoding='utf-8',) as f_r:
    text = f_r.read() #Read the whole file as a single string
    
text= []
with open(f_i, 'r', encoding='utf-8') as f_r:
    for line in f_r:
        text.append(line) #Read the file one line at a time
        
        
#Every line in a text file ocntains a \n at the end (except maybe the last one)
#Sometimes it is useful to remove such \n --> use strip() from strings

text= []
with open(f_i, 'r', encoding='utf-8') as f_r:
    for line in f_r:
        text.append(line) #Read the file one line at a time
        