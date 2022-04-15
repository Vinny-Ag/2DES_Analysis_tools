#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  23 02:50:02 2021

@author: vinny-holiday
"""

import matplotlib.pyplot as plt
import numpy as np
import sys
import math

infile = sys.argv[1]


#data = np.loadtxt(fname='./Vince_2DES/Model_system1/region_01175_0105/_2DES_0.dat')
data = np.loadtxt(fname= infile)
fig, ax = plt.subplots(figsize=(10,10))



X = data[:,0]
Y = abs(data[:,1])

plt.plot(X,Y,'b')
plt.xlabel(sys.argv[2])
plt.ylabel('Intensity (arb.)')
plt.title(infile)
# plt.xticks([2.7,2.8,2.9,3.0],fontsize=13)
# plt.yticks([2.7,2.8,2.9,3.0],fontsize=13)
plt.legend()

plt.show()
