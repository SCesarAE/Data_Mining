#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:05:04 2021

@author: Cesar A. Salgado E.
prigram 09: Dictionaries
"""

#A dictionary is an ordered collection of pairs key:value. They are optimized
#to retrieve information.
#key must be of an immutable type (not a list, set or dictionary)
#keys are unique, there could not be two keys with different values
#value could be of any type
#A dictionary is similar to an array ( or a list), but instead of an 
#index to acces an object, we use a key

d = {}                  #Empty dictionary
d = {'uno': 'value','number':2,3:'test'}    #Dictionary with three pairs
print (d['uno'])                            #The value is accesed by its key
print(d['number'])                          #The object between [] is the key 
#not an index
print(d.get('uno'))                         #Similar to d[key]
d['uno'] = 1478                             #Change the value associated with a
d['uno'] = 'Hello world!'                   #Value ssociated with an existing key is overwritten

d['five'] = 5                               #Add an element to a dictionary, similar
d.update({6:'six','eight':'hello',9:1890})  #Add several elements to a dictionari
d.pop(9)                                    #Remove the pair with the speciied key.
                                #it return the value and delete the pair
print(len(d))       #number of pairs in a dictionary
del d['eight']
d.clear()           #Delete all the pair in a dictionary

l = ['key1','key2', 'key3'] # A list of keys
d = dict.fromkeys(l, 0) #Creates a dictionary using the list of keys an
                        #a value of 0 for all the keys.
                        #Dict is a reserved word for dictionaries
d = dict(brand="ford", model="Mustang", year=1963) #creatin a dictionary
    #with dict
    #Note that keys are not string literals
    #note the use of equals rather than colon for the assigment
    
if 'brand' in d:    #check if a key exist in a dictionary
    print('yes')
    
keys = d.keys() #Return a list with all the keys
values = d.values()#Return a list with all the values
items = d.items() #Return a list fill with tuples of keys, value

#Accesing pairs in a dictionary
#Dictionaries are orderes, the keys are returned in insertion order
for k in d:         #A dictionary is an iterable, we first acces the key
    print(k,d[k])   #Accessing the value associates with the key
    
for k,v in d.items(): #Accessing key and value at the same time
    print(k,v)
    
d_n = {1:'Geeks', 2: 'for', 3:{'A': 'welcome', 'b': 'to', 'C0: Geeks'}} #Nested diccionaries
d_l = {1:['one','two','three'], 2:['four','five','six'], 3:['seven','eight'.'nine']} #A dictionary of lists
