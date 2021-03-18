#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:25:32 2021

@author: Cesar A. Salgado E.
Program 11: Funtions and files
"""

def greet(name):
    """This funtion send a greet to the person that is passed as argument"""
    print('hello' + name + '. Good morning!')
    
greet('Juan')   #calling a funtion

def absolute_value(num, name):
    """This funtion return the absolute value of a number"""
    print('Hello,' + name + '. Good mornig!')
    if num >=0:
        return num, name
    else:
        return -num, name
    
print(absolute_value(-89))
n,m = absolute_value(-89,'maria')
print(n)

#default arguments
def greet(name, msg ='Good morning!', number = 3):
    """This funtion greets a person with the desired message.
    if the mensage is not passed, the default "Goodmorning! is used"
    """
    print('Hello,' + name + ', '+ msg + str(number))
   
greet('maria')
greet('maria', 'how do yu do?')
greet('maria', 'how do yu do?',10)

#Keywords arguments
greet(name='maria', msg='how do yu do?')
greet(msg='how do yu do?', name='Maria',number=10)
greet('maria', number=9 ,msg='how do yu do?')

#Undefined number of arguments
def greet(*names):
    """This funtion greets all the person inside a tuples"""
    for name in names:
        print('hello!',name)
        
greet('Maria', 'luis', 'pedro', 'susana', ['Juan', 'Ana'])


        
