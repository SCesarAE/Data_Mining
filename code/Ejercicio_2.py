#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 17:52:29 2021

@author: Cesar A. Salgado E.

@Description: Leer el archivo con los datos de los estuddiantes y para todas las variables nominales,
encontrar las freccuencias de cada valor, el porcentaje y hacer los graficas de pie y de barra.

En la salida ordenar las frecuencias/porcentajes Ordenados de mayor a menor.
"""

import matplotlib.pyplot as plt
import pandas as pd


#FUNCIONS
def Frecuency(df, Val):
    data = {} #Diccionario con los datos principales y los
    n = 0    
    #Extraction of interest data
    DataVal = df[Val].tolist()
    
    #iteramos sobre nuestra lista de datos
    for i in DataVal:
        #iteramos sobre el contenido del elemento nuestra lista, separando entre comas
        for j in i.split(','):
            #cambiamos el elemento con una copia en minusculas eliminando espacios
            j = j.lower().strip()
            #insetamos al diccionario de datos con 
            data[j] = data.get(j, 0) + 1
            n+=1
    
    #Ordenamiento de datos con funcion lamba
    data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
    
    """Nota: 
    esta funcion nos devuelve una tupla con los datos ordenados, por lo que es necesario
    un cast a diccionario
    
    x es la tupla de nuestros datos
    x[0] es la llave
    x[1] es el valor
    
    """
            
    Dlab = []
    Dval = []
    print(f" \t---{Val}---")
    for i in data:
        Dlab.append(i)
        Dval.append(data[i])
        print(f"{i} : {data[i]} : {data[i]/n*100} %")  
    else:
        print("---------------------------------- \n")
        
    #VISUALIZACION DE DATOS
    #Grafica de Pie
    plt.pie(Dval, labels=Dlab)
    plt.suptitle(Val)    
    plt.figure()
    
    plt.bar(Dlab, Dval)
    plt.suptitle(Val)            
    plt.figure()
    


#DATA READING
w_d = '/home/chicho/Documents/Universidad/DM/DM/data/'
f_i = w_d + 'info_estudiantes.csv'
    
text = []
with open(f_i, 'r', encoding='utf-8') as f_r:
    for line in f_r:
        text.append(line.strip()) #Read the file one line at a time
    
df = pd.read_csv(f_i) #Create a DataFrame from a CSV file    

Nom_lev = ["sexo","color_fav", "mascota","cd_origen", "consola", "cantante_fav"]

#Frecuency(df,'color_fav')
for i in Nom_lev:
    Frecuency(df,i)


