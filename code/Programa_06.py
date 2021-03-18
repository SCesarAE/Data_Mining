#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:12:23 2021

@author: Cesar A. Salgado E.
program 06: String to list to string
"""
sq = 'Hello world! how are you'
words = sq.split()  #Return a list of substrings separated by the given
                    #Delimiter. The delimiter is anothe string,
                    #with no arguments it splits on all whitespace chars
                    #string to list
                    
word2 = ['Hola','mundo!']
s2 = '*'.join(word2)   #Return a string formed by the concatenation of
                        #all the strings in a list separated by
                        #a delimiter '*' ---list to string
                  
#cete a new list with elements from an iterable 
l_letters = []
for char in 'human':
    l_letters.append(char)
print(l_letters)
 
#Using list comprehesion
l_pair =[]
for x in range(20):
    if x %2 ==0:
        l_pair.append(x)
        
        
l_pair = [x for x in range(20) if x%2 ==0] #Select only those number
                                            #from the iterable that are pairs
                                            
#Nested conditionals
#select only those numbers that are pairs and divisible by 5
l_numbers = [y for y in range(100) if y%2 == 0 if y%5 ==0]
l_numbers = []
for in range(100):
    if y % 2 == 0:
        if y %5==0:
            l_numbers.append(y)
            
#Alternatively, use logical operators
#does the same as above
l_numbers = [y for y in range(100) if y%2 == 0 if y%5 ==0]
l_numbers = []
for in range(100):
    if y % 2 == 0 and y % 5 ==0:
            l_numbers.append(y)

#if.. else
#create a list full of string 'even or 'odd' id the numbers are pairs on not
l_number = ['even' if %i%2 ??0 else 'odd' for i in range(10]
                                                         
#important
#1. List comprehension is an elegant way to define and create list based on existing iterables.
#. list comprehension is generally more compact and faster than normar functions
#and loops for ceating list.
#3. However, we should acoid writing vey long list conprehensions in one line to ensure that code is user-friendly.
#. Every list comprehension can be rewritten in a for loop, but
#nor every for loop can be rewritten as a list comprehension.