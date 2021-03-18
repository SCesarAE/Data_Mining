#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:26:35 2021

@author: Cesar A. Salgado E.

Program 05= Object identifiers and string (as lists)
"""

a = 5
print(id(a))        #id od an object

b = 6
print(id(b))

b = 5       
print(id(b))        #Referen to an object that already exists

a= [1,2,3]          #New collection of objects
print(id(a))

b = a                #Reference to an existing object
print(id(a))        #id of the referenced object

b.append(4)         #modified the referenced object
print(a)
print(b)

b = []              #create a new object
b.extend(a)
b.append(5)
print(id(b))


#Strings are inmutable lists
#the objects (chracter) in a specific index CANNOT be modified
s = 'hello world!'
print(s)
print(s[3])     #Character at index 3
print(s[:5])    #Slicing: characters from index 0 to 5-1
print(s[5:])    #Slicing: characters from index 5 to end
print(s[:5:2])    #Slicing: characters from the begining, end, step
s[5] = 'd'      #not possible because strings are inmutable

s = 'hello'
t = 'world!'
u = s + ' ' + t #concatenation
print(s*3)      #repetition
print(len(u))   #lenght of string

#comparing strings
a = 'Hello world!'
if a == u:
    print('yes')
    
s = 'hello'
a = 'hello'
if a > s:           #Comàrison is done lexicographically i.e using
                    #ASCII value of the characters
    print('yes')
elif a < s:
    print('no')
else:
    print('son iguales')

#iterates over string
for i in s:     #i iterates over the characters of the string. a string is a 
    print(i)    #i takes the character in order ( a strsing is a list, then

for i in s[2:4]:
    print(i)

for  i in s[::-1]:  #i iterates over the string form end to begining
    print(i)
    
#Some useful string methods
#strings are inmmutable, so the methods alwaus return anothe string
#they do not modify the cuttent string.
s1 = '  Hello world from python world \t \n'
print('\n', s1.lower())         #Return the lowecase version of the string
print('\n', s1.upper())         #Return the uppercase version of the string
print('\n', s1.strip())         #Return a string with whitespace removed from the start and end
print('\n', s1.lstrip())         #Return a string with whitespace removed from the  start
print('\n', s1.rstrip())         #Return a string with whitespace removed from the end
print('\n', s1.isalpha())         #Test if all the chars in the string are alphabetic chars
print('\n', s1.isdigit())         #Test if all the chars in the string are digit
print('\n', s1.isspace())         #Test if all the chars in the string are spaces
print('\n', s1.isspace())         #Test if the string starts with the given othe string
print('\n', s1.isspace())         #Test if the strings ends withs the given other string
print('\n', s1.isspace())         #Test if the strings ends with the given other strings
print('\n', s1.isspace())         #Search for the given other string within s1, and returns the first index
print('\n', s1.isspace())         #R


            