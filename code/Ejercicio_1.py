#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 15:33:11 2021

@author: Cesar A. Salgado Escoto

@Description: Leer el archivo con los datos de los estudiantes y para la variable color
y semestre encontrar las frecuencias de cada valor, el porcentaje y en el caso del semestre 
la media.

Color
rojo: 25:10%
amrarillo:40:17%
rosa:10:%4%

Semester
1:2:2%
2:5:4%
8:40:40%

Media semestre: 7.2
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


#Funcion para tratamiento de datos
def DataProcessNV(listOrg, TypeF):
    listD = []
    
    #Convercion a string
    listAux = ",".join(listOrg)    
    #Eliminacion de caracteres de escape
    listAux = listAux.replace('\n','')
    listAux = listAux.replace('\t','')
   
    #Convercion a lista y eliminacion de espacios
    listAux = listAux.rsplit(',')
    
    for i in listAux:
        if ( i.find(" ") == 0 ):
            i = i[1:]

        if( i.endswith(" ")):
            i = i[:-1]

        listD.append(i)
    
    
    NoData = len(listD)
    Pr_Data = []
    FrData = []
    PData = []
    
    #Contador para frecuencia acumulada
    if( TypeF == "F_Acu"): 
        nAcu = 0 

    #Lista de los datos principales    
    Pr_Data = []
    for i in listD:
        if (Pr_Data.count(i) == 0):
            Pr_Data.append(i)
        else: continue
    
    for i in Pr_Data:
        #Porcentaje
        PData.append(float(format((listD.count(i)/NoData)*100, '.2f')))
    
        if (TypeF == "F_Rel" ):
            FrData.append(str(listD.count(i) + "/" + str(NoData)))
              
        elif( TypeF == "F_Acu" ):
            nAcu += int(listD.count(i)) 
            FrData.append(nAcu)
        else:
            FrData.append(listD.count(i))    
    
    return listD, Pr_Data, FrData, PData 



# Procesamiento de Datos Variables y Calculos Estadisticos
def DataProcessIV(listOrg,TypeFre):
    #Tratamiento de datos
    listD = list(listOrg)
    NoData = len(listD)
    PorData = [] #Porcentaje de los datos
    FreData = [] #Frecuencia de los datos
    MediaD = 0 #Media de los datos
    
    #Contador para frecuencia acumulada
    if(TypeFre == "F_Acu"): 
        nAcu = 0
    
    #Extraccion datos principales y Calculo de la media (Para aprovechar el for)
    Pr_Data = []
    for i in listD:
        MediaD += i
        if( Pr_Data.count(i) == 0 ):
            Pr_Data.append(i)
        else:
            continue
    else:
        MediaD = format(MediaD/NoData,".2f")
    
    #Ordamiento de los datos principales
    Pr_Data.sort()
    
    #Calculo de frecuencias y porcentaje
    for i in Pr_Data:
        #Porcentaje
        PorData.append(float(format((listD.count(i)/NoData)*100, '.2f')))
    
        if (TypeFre == "F_Rel" ):
            FreData.append(str(listD.count(i) + "/" + str(NoData)))
              
        elif( TypeFre == "F_Acu" ):
            nAcu += int(listD.count(i)) 
            FreData.append(nAcu)
        else:
            FreData.append(listD.count(i))    
    
    return Pr_Data, FreData, PorData, MediaD



#Visualizacion de informacion
def DataDisplay(Name,Pr_Dt, FreDt, PorDt):
    print("-----------------------------------------")
    for i,j,k in  zip(Pr_Dt, FreDt, PorDt):
        print(f"{i} : {j} -> {k} %") 

    #VISUALIZACION DE DATOS
    #Grafica de Pie
    plt.pie(FreDt, labels=Pr_Dt)
    plt.suptitle(Name)
    
    plt.figure()
    plt.bar(Pr_Dt, FreDt)
    plt.suptitle(Name)


#---------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------
#EXTRACION DE DATOS VARIABLES INTERVALOS
#Edad
Pr_Edad, FreE, PorE, MediaE = DataProcessIV(df["edad"], "Fr_Abs")
print(f"La media de la edad es: {MediaE}")
DataDisplay("Edad", Pr_Edad, FreE, PorE)

#Altura
Pr_Altura, FreAl, PorAl, MediaAl = DataProcessIV(df["altura"], "Fr_Abs")
print(f"La media de la edad es: {MediaAl}")
DataDisplay("Altura", Pr_Altura, FreAl, PorAl)

#Peso
Pr_Peso, FreP, PorP, MediaP = DataProcessIV(df["peso"], "Fr_Abs")
print(f"La media de la edad es: {MediaP}")
DataDisplay("Peso", Pr_Peso, FreP, PorP)

#Semestre
Pr_Semestre, FreSe, PorSe, MediaSe = DataProcessIV(df["semestre"], "Fr_Abs")
print(f"La media de la edad es: {MediaSe}")
DataDisplay("Semestre", Pr_Semestre, FreSe, PorSe)

#No. Curso
Pr_NoCurso, FreNoC, PorNoC, MediaNoC = DataProcessIV(df["num_cursos"], "Fr_Abs")
print(f"La media de la edad es: {MediaNoC}")
DataDisplay("No. Cursos", Pr_NoCurso, FreNoC, PorNoC)


#EXTRACION DE DATOS VARIABLES NOMINALES
#Sexo
Sexo, Pr_Sexo, FreSx, PorSx = DataProcessNV(df['sexo'],"F_Abs")
DataDisplay("Sexo", Pr_Sexo, FreSx, PorSx)

#Color 
Colors, Pr_Colors, FreC, PorC = DataProcessNV(df['color_fav'],"F_Abs")
DataDisplay("Colores", Pr_Colors, FreC, PorC)

#Mascotas
Mascotas, Pr_Mascotas, FreM, PorM = DataProcessNV(df['mascota'],"F_Abs")
DataDisplay("Mascotas", Pr_Mascotas, FreM, PorM)

#Ciudad de Origen
CiudadOrg, Pr_CiudadOrg, FreCO, PorCO = DataProcessNV(df['cd_origen'],"F_Abs")
DataDisplay("Ciudades", Pr_CiudadOrg, FreCO, PorCO)

#Consola
Consola, Pr_Consola, FreCon, PorCon = DataProcessNV(df['consola'],"F_Abs")
DataDisplay("Consolas", Pr_Consola, FreCon, PorCon)


#Cantante o Banda
Cantante, Pr_CoB_Fav, FreCB, PorCB = DataProcessNV(df['cantante_fav'], "F_Abs")
DataDisplay("Bandas y Cantantes", Pr_CoB_Fav, FreCB, PorCB)


#---------------------------------------------------------------------------------------------------
# Codigo Original
"""
def DataProcessNV(listOrg):
    listD = []
    
    #Convercion a string
    listAux = ",".join(listOrg)    
    #Eliminacion de caracteres de escape
    listAux = listAux.replace('\n','')
    listAux = listAux.replace('\t','')
   
    #Convercion a lista
    listAux = listAux.rsplit(',')
    
    for i in listAux:
        if ( i.find(" ") == 0 ):
            i = i[1:]

        if( i.endswith(" ")):
            i = i[:-1]

        listD.append(i)
    
    return listD

#Funcion para calcular frecuencias
def FrecuencyNV(listD, TypeF):
    NoData = len(listD)
    Pr_Data = []
    FrData = []
    PData = []
    
    #Contador para frecuencia acumulada
    if( TypeF == "F_Acu"): 
        nAcu = 0 

    #Lista de los datos principales    
    Pr_Data = []
    for i in listD:
        if (Pr_Data.count(i) == 0):
            Pr_Data.append(i)
        else: continue
    
    for i in Pr_Data:
        #Porcentaje
        PData.append(float(format((listD.count(i)/NoData)*100, '.2f')))
    
        if (TypeF == "F_Rel" ):
            FrData.append(str(listD.count(i) + "/" + str(NoData)))
              
        elif( TypeF == "F_Acu" ):
            nAcu += int(listD.count(i)) 
            FrData.append(nAcu)
        else:
            FrData.append(listD.count(i))    
    
    return Pr_Data, FrData, PData 


#EXTRACION DE DATOS
ColorsOri = df['color_fav'].tolist()

#TRATAMIENTO DE DATOS
#Convercion a string
Colors  = ",".join(ColorsOri)

#Eliminacion de caracteres de escape
Colors = Colors.replace('\n','')
Colors = Colors.replace('\t','')
Colors = Colors.replace(' ','')

#Convercion a lista
Colors = Colors.rsplit(',')


#Colores principales 
Pr_Colors = []
for i in Colors:
    if (Pr_Colors.count(i) == 0):
        Pr_Colors.append(i)
    else: continue

        
#CONTEO DE COLORES
NoColors  = len(Colors)
ValC = []
print("\t Colors")
for i in Pr_Colors:
    ValC.append(Colors.count(i))
    #print(i,':', Colors.count(i), ':', format((Colors.count(i)/NoColors)*100, '.2f'),'%')
    print(f"{i} : {Colors.count(i)} -> {format((Colors.count(i)/NoColors)*100, '.2f')} %") 

#VISUALIZACION DE DATOS
#Grafica de Pie
plt.pie(ValC, labels=Pr_Colors)
plt.figure()
plt.bar(Pr_Colors, ValC)

#Frecuencias
print("\n\t\t Tabla de Frecuencias")
print("-------------------------------------------------")
print(" \t \t F.Absoluta | F.Relativa | F.Acumulada")
Ac = 0
for i in Pr_Colors:
    n = Colors.count(i)
    Ac += n      
    print(f"{i} \t | \t {n} \t | \t {n}/{NoColors} \t | \t {Ac}")



#---------------------------------------------------------------------------------------------------

#EXTRACION DE DATOS
#Semestre
Semester = df['semestre']

#Tratamiento de datos
Semester = list(Semester)
#Semester.sort()

#Semestres Principales
Pr_Semester = []
for i in Semester:
    if( Pr_Semester.count(i) == 0 ):
        Pr_Semester.append(i)
    else:continue

#Ordenamiento
Pr_Semester.sort()
NoSemester = len(Semester)
ValS = []
for i in Pr_Semester:
    ValS.append(Semester.count(i))
    print(f'{i}º Semestre: {Semester.count(i)} -> {format((Semester.count(i)/NoSemester)*100,".2f")} %')


#VISUALIZACION DE DATOS
#Grafica de Pie
plt.pie(ValS, labels=Pr_Semester)
plt.figure()
#Grafica de Barras
plt.bar(Pr_Semester, ValS)



#Frecuencias
print("\n\t Tabla de Frecuencias")
print("-------------------------------------------------")
print(" \t F.Absoluta | F.Relativa | F.Acumulada")
Ac = 0
for i in Pr_Semester:
    n = Semester.count(i)
    Ac += n      
    print(f"{i} \t\t {n} \t\t\t {n}/{NoSemester} \t\t\t {Ac}")
    
#Media
media = 0 
for i in Semester:
     media += i
else:
    print(f'\n Media: {format(media/NoSemester,".2f")}')
"""



