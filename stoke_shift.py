#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 02:43:42 2021

@author: vinny-holiday
"""



import matplotlib.pyplot as plt
import numpy as np
import sys


# FC HARMONIC
# fname=('Decoupled_Morse_harmonic_FC_transient_absorption_spec.txt')
# data = np.loadtxt(fname)

# print(max((data[150*200:150*201,2])))
# # 0.007622859992205522	2750.4344452763144 absorption peak 400 fs delay
# # -0.0011969741256685346	1633.420471811007  Emission: energy,intensity
# print((data[150*200:150*201,2]))

# print(max((data[0:150,2])))
# # 0.006152887639226515	3068.393958279207 absorption peak  0 fs delay

# stoke shift = 0.0049559


#CUMULANT
# filename=('Decoupled_Morse_cumulant_2nd_order_cumulant_transient_absorption_spec.txt')
# data_cum = np.loadtxt(filename)
# print(max((data_cum[150*200:150*201,2])))
# print((data_cum[150*200:150*201,2]))
# -0.0053898986275897065	405.28428058055135 absorption peak 400 fs delay
# -0.06425004159479093	375.97380619669343  Eission energy, intensity 

# print(max((data_cum[0:150,2])))
# 0.0053898986275897065	747.1038562237798 absorption peak 0 fs 

# stoke shift = 0.0053898986275897065 +(-0.06425004159479093) = 0.0588


#EXACT
file = ('Decoupled_Morse_Exact_transient_absorption_spec.txt')
data_ex = np.loadtxt(file)

print(max((data_ex[150*200:150*201,2])))
print((data_ex[150*200:150*201,2]))
-0.02162084335839963	1970.302805532265 absorption peak 400 fs delay
-0.07166115220772679	-1705.455460825012 Emission peak ??

print(max((data_ex[0:150,2])))
-0.009983562230649126	1498.6087153398455 absorption peak 0 fs 

# stoke shift = -0.009983562230649126 - (-0.07166115220772679) = 0.06167759