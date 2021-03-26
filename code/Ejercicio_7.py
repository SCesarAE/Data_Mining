#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:53:21 2021

author: Cesar A. Salgado E.

@Description: Leer el archivo con los datos de los estudiantes y para todas las variables 
intervalo/razon,obtener el resumen de lis cinco números:
mínimo, máximo, 1er cuartir, mediana, 3er Cuartil ( graficar el boxplot)

Para cada variable, separar la lista de valores en n bins. La salida es un lista de listas
con los valores que correspondan a cada bin


lista = [1.75, 1.63, 1.89, 1.93, 1.56, 1.72, 1.65, 1.80, 1.77, 1.71]
n = 3
outpur = [[1.56, 1.63, 1.65], [1.71, 1.72, 1.75, 1.77, 1.8],[1.89, 1.93]]
"""

import matplotlib.pyplot as plt
import pandas as pd
import math as mt


#Funcion de calculo de bins
def bins(values, n_bins):
    #ordenamiento de los datos
    values.sort()
    
    mx = values[-1] #Maximo
    mn = values[0]  #Minimo
    
    rang = mx - mn #Rango
    inc = rang/n_bins #intervalo
    
    #Definimos una lista de listas(vacia)
    bins = [[]]
    count = 0
    
    #limite superior del bins
    ul = mn + inc
    
    #ciclo para llenar la lista 
    for i in values:
        #comprobamos si se exede el limite inferio
        if i > ul:
            bins.append([])
            count += 1 #aumenta contador
            ul+=inc #aumenta el limite superior
        
        bins[count].append(i)
    
    return bins



#Funcion para cortar valores
def trim_data(values, a):
    n = len(values) 
    k = int(a/100*n) #Porcentaje de recorte
    
    #regresamos nuestra lista recortada mediante slicing
    return values[k:n-k]

def var_std(values):
    #Calculo de la media
    media = sum(values)/len(values)
    n = len(values)
    #calculamos numerador de la divicion
    num = [(i-media)**2 for i in values] #Compresion de listas
    num = sum(num)
    #calculamos varianza
    var = num/(n-1)
    #Calculo de la desviacion estandar
    std = mt.sqrt(var)
    
    return var, std

def percentil(values, per):
    #Calculamos la posicion
    pos = (len(values)-1)*per
    
    #Limite inferior y superios
    pl = mt.floor(pos)
    pu = mt.floor(pos)
    
    return values[pl]+(values[pu]-values[pl])*per

def outliers(values, fq, tq):
    iqr = tq - fq
    uif = tq + 1.5 * (iqr)
    lif = fq - 1.5 * (iqr)
    
    #Ciclo para encontrar el lower inner fance
    for i in values:
        if i >= lif:
            lw = i
            break
    #Ciclo para encotrar el upper inner fanse 
    #(la lista se encuetra ordenada por lo que se recorre en orden inverso)
    for i in values[::-1]:
        if i <= uif:
            uw = i
            break
    #Calculamos outliers
    outs =[]
    for i in values:
        #Si se encuentran fuera del upper inner fanse y de lower inner fanse
        #entonces seran aoutliers
        if i < lw or i > uw:
            outs.append(i)
            break
        
    return iqr, lw, uw, outs

def summary(data): 
    n = len(data) #Total de valores
    index = list(range(n)) #lista con los indices de los pocibles valores
    
    #Grafica Natuarl 
    plt.scatter(index,data)
    plt.suptitle("Naturales")    
    plt.figure()
    
    #Grafica Ordenada
    data.sort() #ordenamiento de los datos
    plt.scatter(index,data)
    plt.suptitle("Datos Ordenados")    
    plt.figure()
    
    #Buscaqueda de Minimo Maximo
    """
        Al ordenar nuesta lista el maximo y el minimo se encontraran al final
        y al principio de nuestra lista. Esto se visualiza en la grafica scatter 
    """
    mn = data[0] 
    mx = data[-1] 
    fq = percentil(data, 0.25) #Primer cuartil
    med = percentil(data, 0.5) #Mediada
    tq = percentil(data, 0.75) #Tercer cuartil
    print(f' Minimo: {mn}')
    print(f' Maximo: {mx}')
    print(f' 1er Cuartil: {fq:.3f}')
    print(f' Mediana: {med:.3f}')
    print(f' 3er Cuartil: {tq:.3f}')
    
    #MEdia
    md = sum(data)/len(values)
    print(f'Media = {md:-3f}')
    var, std = var_std(data)
    print(f'Varianza = {var:-3f}')
    print(f'Desviacion estandar = {std:-3f}')
    
    #Grafica Boxplot
    plt.figure()
    plt.boxplot(data)
    plt.suptitle("Boxplot")   
    
    #Modificacion del Boxplot
    #iran q, lower wisker, uper wisker, outliers
    irq, lw, uw, outs = outliers(data, fq, tq)
    
    #imprimimos los valores
    print(f' IRQ: {irq}')
    print(f' LW: {lw}')
    print(f' UW: {uw}')
    print(f' Outs: {outs}')
    
    #Impresion de bins
    n_bins = 5
    bis = bins(data, n_bins)
    print(f'Los bins son: {bis}')
    
    #Grafico de los bins
    plt.figure()
    plt.hist(data, n_bins)
    plt.suptitle("Grafica de bins")  
    

#DATA READING
w_d = '/home/chicho/Documents/Universidad/DM/DM/data/'
f_i = w_d + 'info_estudiantes.csv'
    
text = []
with open(f_i, 'r', encoding='utf-8') as f_r:
    for line in f_r:
        text.append(line.strip()) #Read the file one line at a time
    
df = pd.read_csv(f_i) #Create a DataFrame from a CSV file    

#Int_lev = ["edad","altura", "peso", "semestre", "num_cursos"]
lv = ["edad"]

for i in lv:
    values = df[i].tolist()
    summary(values)
    print(f"*********** Trimed data for {i}*******")
    values = trim_data(values, 10)
    summary(values)
    print("----------------------------------------")

