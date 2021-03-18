#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:12:57 2021

@author: Cesar A. Salgado E.
Program 10: Random number
"""

import random as rn

#Random numbers
rn.random()                 #return the next random floating poin numbre in the range[0.0, 1.0]

rn.uniform(2.5, 7.8)        #Return a random floating point numbre N between a and b

rn.seed(90.89)              #initialize internal state of the random number generator.

rn.gettrandbits(9)          #Return a python int with k random element from range(start, stop)
rn.randrange(100,200)       #Return a randomly selected element from range(start, stop, step)
rn.randint(100,200)         #Return a random integer N such that a <=N <= b

x =['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c']
rn.choice(x)                #Return one element at random from iterable
rn.shuffle(x)               #Shuffle the sequence in place
rn.sample(x,3)              #Return a k length list of unique elements chosen from sequencce

