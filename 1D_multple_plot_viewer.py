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


# sys.argv[1] = 2DES file name w/o the number.dat
# sys.argv[2] = number of spectra to iterate over
# sys.argv[3] = x-axis label

infile = sys.argv[1]

fig, ax = plt.subplots(figsize=(10,10))

num_spectra = int(sys.argv[2])
counter = 0
for i in range(num_spectra):
	data = np.loadtxt(fname=str(infile)+str(counter)+'.dat')
	X = data[:,0]
	Y = data[:,1]**2
	counter = counter + 10
	plt.plot(X,Y, color='g')
plt.xlabel(sys.argv[3],fontsize=15)
plt.ylabel('Intensity (arb.)')
plt.title('infile')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend()
plt.show()
# plt.xticks([2.7,2.8,2.9,3.0],fontsize=13)
# plt.yticks([2.7,2.8,2.9,3.0],fontsize=13)

