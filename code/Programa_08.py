#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:36:24 2021

@author: Cesar A. Salgado E. 
Program 08: Tuples and sets
"""

#Python tuples
t = ('tuples', 'are','list', 'but', 'immutable', 4, [1,2]) #tuples definition
print(t[0])     #indexing
print(t[:3])   #Slicing
t[0] 0 'assignement to elements in a tuple are not possible'
#tuples ar inmutables
t = t +(9,) #merge of tumples. the ',0 is necesary to indicate to python
t = t[:-1]
t =t[:2]+ t[4:]
print('\nAdd several elements to tuples')
t = t+(10,11,'hello',10) #Merge of tuples. The '' is no longer necessary
print(t.index(10))  #Returns the index of the first occurence of object
print(t.count(10))  #Return the number of defined objects
t_2 = t*2           #Repetition of tuples


t_3 = ('a', 'b')
x,y = t_3           #Tuples unpacking. Each object in the left takes an object

a = [(1,2),(3,4), (5,6)]    #A list of tuples
b = ([1,2],[3,4], [5,6])    #A tuples of lists
c = tuple(a)               #List to tuples
d = list(b)                 #Tuples to list

for i in t:              #tuples are iterables
    print(i)

for i in range(len(t)): #But can also he accesd by index
    print(t[i])
    
#Typls are faste than list. They are useful when a collection of objects are
#not going to change during the program execution.


#Python sets
a = {}                  #Empty set {no es cierto}
a = {1,2,3,4,5.5,1,2,3} #Set definition
a 0 {5,1,,2,3,3,4,5,5,3,2,1}    #Collection of unique objects,
                                #repeated objects are liminated
print[0]                        #Collection of unordered objects,
                                #so we cannot acces objects by index
b = {3,4,5,6,7,8}
print(a.union(b))               #Return a set tht is the union of two
print(a.intersectio(b))         #Return a set that is the intersection
print(a.difference(b))          #Return a set that is the difference of two sets
print(a.difference(b))

b={1,2}
print(b.issubset(a))            #Return tru if b is a subset of a
print(b.issuperset(a))          #Return tru if b is a superset of a
a.add('hola')                   #Add object to a set
u.update(['one', 'two','three'])#add a list of objects to set
a.remove(3)                     #Remove an object from a set(objects a)
a.pop()                         #Extract the last object from the set. since sets are
                                #don't kwon which object will be extracted
                                
for i in a:                     #Sets are iterables
    print(i)                    #But cannot be accessed by index
    

                                
 