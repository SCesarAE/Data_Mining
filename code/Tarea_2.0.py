
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:59:28 2021

Leer el archivo con los datos de los estudiantes y para
todas las variables nominales, encontrar las frecuencias de cada
valor, el porcentaje y hacer las graficas de pie y de barra.

Variables nominales
nombre
sexo
color_fav
mascota
cd_origen
consola
cantante_fav

En la salida, devolver las frecuencias/porcentajes ordenados
de mayor a menor

@author: melyk
"""


import matplotlib.pyplot as plt
import pandas as pd

w_d = '/home/chicho/Documents/Universidad/DM/DM/data/'
f_i = w_d + 'info_estudiantes.csv'


text = []
with open(f_i, 'r', encoding='utf-8') as f_r:
        for line in f_r:
            text.append(line.strip()) #Read the file one line at a time

df = pd.read_csv(f_i) #Create a DataFrame from a CSV file

S = df['semestre']
#EXTRACION DE DATOS
sexo = df['sexo'].tolist()
colors = df['color_fav'].tolist()
mascota = df['mascota'].tolist()
cantante_fav = df['cantante_fav'].tolist()
cd_origen = df['cd_origen'].tolist()
consola = df['consola'].tolist()

#Declaracion de las funciones
def TabulacionesOrdinal(lista):
    
    #Tratamiento de datos
    lista = list(lista)
    #Semestres Principales
    NL = []
    for i in lista:
         if( NL.count(i) == 0 ):
             NL.append(i)
         else:continue

    #Ordenamiento
    aux=0
    aux2=0
    media=0
    NL.sort()
    NoSemester = len(lista)
    for i in NL:
        print(f'{i}º Semestre: {lista.count(i)} -> {format((lista.count(i)/NoSemester)*100,".2f")} %')
        n = lista.count(i)
        aux += n 
        aux2 += NL.count(i)
        #Hacer la media
    media = aux/aux2
    print("La media es:",media)
   

def TabulacionesNominales(lista):
    
    d ={} #Se crea vacio para hacer un nuevo almacenaje
    n=0

    for i in lista:
        for c in i.split(','):
            c=c.lower().strip() 
            d[c] = d.get(c, 0) + 1 #Se añaden al nuevo arreglo
            n += 1
        
        lab = []
        val = []
        for i in d:
            lab.append(i)
            val.append(d[i])
            print(i, ':', d[i],':',d[i]/n*100,'%')
        
   

def graficar(lab,val):
    plt.pie(val,labels=lab)
    plt.figure()
    plt.bar(lab,val)
    
    
def limpiezadedatos(lista):
    L  = ",".join(lista)
    L = L.replace('\n','') #Saltos de linea
    L = L.replace('\t','') #tabulaciones
    L = L.replace(' ','') #espacios


#Se le ingresan los datos a desear
TabulacionesNominales(colors)
#graficar(lab,val)
TabulacionesOrdinal(S)
