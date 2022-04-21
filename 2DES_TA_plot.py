#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:07:27 2020

@author: vinny-holiday
"""

import matplotlib.pyplot as plt
import numpy as np
import sys

infile = sys.argv[1]

#data = np.loadtxt(fname='./Vince_2DES/Model_system1/region_01175_0105/_2DES_0.dat')
data = np.loadtxt(fname= infile)
fig, ax = plt.subplots(figsize=(10,10))

X = data[:,0].reshape(3,3000)*(0.024188)
Y = data[:,1].reshape(3,3000)*27.2114
Z = data[:,2].reshape(3,3000)

plt.contourf(X,Y,Z, 1000)
plt.colorbar()

plt.show()



