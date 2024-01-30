#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:25:40 2024

@author: brettnakao
"""

import numpy
import numpy as np
print("What is the mass of the box") #input for m
m = float(input())
print("What is the coefficient of kinetic friction") #input for u
u = float(input())
print("What is the angle of the surface in radians") #input for theta
theta = float(input())

g = 9.8

F = float(u*m*g*np.cos(theta)) #defining force of friction F

print("The force of friction acting on the box is " + str(F) + " N")