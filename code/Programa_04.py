#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:38:00 2021

@author: Cesar A. Salgado E.

Program 04= List
"""

#Lists are ordered collection of objects --> Insertion order matter -->
#objects are indexed
#We can accesss objects by index
#objects in a list do not have to be of the same type
#Lists are mutable objects. We can change the objects in specific indexes

a = [1, 2, 3 ,4 ,5, 6 ,7, 8, 9,10]  #A list of int objects
b = [1, 2.2, 'python', [1,2,3]]     #A list of different object
c = []                              #A empty list

print(a)
print(b)
print(a[0])         #Access the object at index 0
print(a[:5])        #Slicing: access the object the index 0 to 5-1
print(a[5:])        #Slicing: access the object the index 5 to end
print(a[2:8:2])     #Slicing: access the object the index 2 to 8-1 in steps of 2

print(a[-1])        #Access the last element
print(a[-2])        #Access the second-to-last element
print(a[-5])        #
print(b[3][2])      #Access the first element of the list inside the first list
b[1] = 'hundread'   #Change the value of element in give index
                    #(lists are mutable)  
                    
b.append('two hundred')     #Add an object to the list at the end
c.append('hello')           #Add an object to the empty list at the end
b.extend('a','b','c','d')   #Extend a list with another list
d = b + ['e','f','g','h']   #Extend a list with another list, concatenation
                            #(not recommended), this create a new list 
                        
b.append(['i','j','k'])
print(len(b))              #Length of list(number of objets in the list)
last = b.pop()             #Extract the last object form the list
fifth = b.pop()            #Extract the object at a given index
print(b)

b.append('a')
print(b)
b.remove('a')               #remove the first occurence of 'a'
print(b)
print(b.index('b')          #Get the index of the first occurence of an object
print(b.index('b',2,5)      #Get the index of the first occurence of an objet
                            #between two index
b.insert(3,2000)            #Inser an object in a specific index
print('a' in b)             #Membership operator(test if a object is inside a colllection)
print('a' not in b)         #Membership operator(test if a object isn't inside a collection)
e = a + b                   #concatenation
e = a*3                     #Repetition: the list is repaeated 3 times

lista = [1,2,3,4,5,6,7,8,9,1,1,1,'q','b','hello',[4,5,'h']]
print(lista.count(1))    #count the number of times an object appears in a list
lista = [1,2,3,4,5,6,7,8,9,1,1,1]
print(lista.sort(reverse=True))     #Sort the object in the list in place(it
                                    #reverse have to be of the same type
print(lista.reverse())              #reverse the order of the objects in the list in place
lista.clear()                       #Remove all items from the list.


#iterate over lists
for i in lista: #i iterates over the objects of the list. A list is an 
                #iterable object
    print(i)    #objects are accesed in order( a list is a ordered collection)

for i in lista[8:]:     #i iterates over a slice of the list.
    print(i)
    
for i in list[::-1]:     #i iterates over the list form end to begining
    print(i)

a = lista[8:]
a.reverse()
for i in a:
    print(i)
    
lista 0 [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
for i in lista:     #i iterates over the objects of lista
    print(i)        #i takes each objects from lista(i is a list)
    
for i in lista:     #i iterates over the objects of lista
    for j in i:     #j itarates over the objects of i
        print(j)    #