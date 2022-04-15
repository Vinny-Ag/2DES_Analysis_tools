#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 16:01:36 2022

@author: vinny-holiday
"""


import numpy as np
import sys
import cmath
import math
import scipy
import decimal
from scipy import integrate

# sys.argv[1] = 2DES file name
# sys.argv[2] = omega 1 energy slice value in eV
# sys.argv[3] = 2DES frame number

data2 = np.loadtxt(fname=sys.argv[1])

def find_nearest(array, value):
	array = np.asarray(array)
	idx = (np.abs(array - value)).argmin()
	return array[idx]

omega1 =  float(sys.argv[2])/27.2114
omega_round = round(omega1,4)
omega_value = find_nearest(data2[:,0],omega_round)

energy_index = (np.where(data2[:,0]==omega_value))
omega_array = np.asarray(energy_index)

omega_3_vals = data2[min(omega_array[0,:]):max(omega_array[0,:]),1]
omega_intensity = data2[min(omega_array[0,:]):max(omega_array[0,:]),2]
print(omega_intensity[2])
print(omega_array)
slice_array = np.zeros((len(omega_array[0,:])-1,2))
# print(slice_array.shape)
for i in range(len(omega_3_vals)):
	slice_array[i,0]= omega_3_vals[i]
	slice_array[i,1]= omega_intensity[i]

np.savetxt('Omega3_slice'+'_'+sys.argv[2]+'eV'+'_'+'frame_'+sys.argv[3]+'.dat',slice_array)
