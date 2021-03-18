#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:47:35 2021

@author: Cesar A. Salgado E.

@Description: Leer el archivo con los datos de los estudiantes y para todas las variables 
intervalo/razon,obtener una grafica de dispersión natural y otra ordenada
"""

import matplotlib.pyplot as plt
import pandas as pd


def summary(df,Val): 
    data = df[Val].tolist()
    n = len(data) #Total de valores
    index = list(range(n)) #lista con los indices de los pocibles valores
    
    #Grafica Natuarl 
    plt.scatter(index,data)
    plt.suptitle(Val+"(Natural)")    
    plt.figure()
    
    #Grafica Ordenada
    data.sort() #ordenamiento de los datos
    plt.scatter(index,data)
    plt.suptitle(Val+"(Ordenado)")    
    plt.figure()

#DATA READING
w_d = '/home/chicho/Documents/Universidad/DM/DM/data/'
f_i = w_d + 'info_estudiantes.csv'
    
text = []
with open(f_i, 'r', encoding='utf-8') as f_r:
    for line in f_r:
        text.append(line.strip()) #Read the file one line at a time
    
df = pd.read_csv(f_i) #Create a DataFrame from a CSV file    

Int_lev = ["edad","altura", "peso", "semestre", "num_cursos"]

for i in Int_lev:
    summary(df, i)
