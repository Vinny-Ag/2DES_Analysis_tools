#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:57:00 2020

@author: vinny-holiday
"""



import matplotlib.pyplot as plt
import numpy as np
import sys

infile = sys.argv[1]

#data = np.loadtxt(fname='./Vince_2DES/Model_system1/region_01175_0105/_2DES_0.dat')
data = np.loadtxt(fname= infile)
fig, ax = plt.subplots(figsize=(10,10))

X = data[:,0].reshape(100,100)*27.211396132+1.7199999999999995
Y = data[:,1].reshape(100,100)*27.211396132+1.7199999999999995
Z = data[:,2].reshape(100,100)

plt.title(infile[0:24])
plt.contourf(X,Y,Z, 100,cmap='plasma')
plt.colorbar()

plt.show()
