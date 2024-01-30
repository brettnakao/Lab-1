#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:17:12 2024

@author: brettnakao
"""

print("What is the initial velocity") #input for v
v = float(input())

g = 9.8

h = float((v**2)/(2*g)) #defining max height h

print("The maximum height is " + str(h) + " m")