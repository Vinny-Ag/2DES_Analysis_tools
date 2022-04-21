#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 16:01:36 2022

@author: vinny-holiday
"""


import numpy as np
import sys
import decimal



data2 = np.loadtxt(fname='Decoupled_Morse_cumulant_2DES_0.dat')
max_intensity_0fs = max(data2[:,2])
energy_index,intensity_max = (np.where(data2==max_intensity_0fs))
print('max energy',data2[energy_index,1])
infile = sys.argv[1]

Num_2DES_frames = 59 #total number of frames you have to iterate over
Delay_time_step = 10 #time step in fs between each 2DES frame

max_list = np.zeros((Num_2DES_frames,2))
time_counter = 0
for i in range(Num_2DES_frames):
    # data = np.loadtxt(fname='Decoupled_Morse_2DES_Exact_'+str(i+1)+'.dat')
    data = np.loadtxt(fname=str(infile)+str(i+1)+'.dat')
    
    max_intensity = data[int(energy_index),2]
    

    #print('max_value: ',max_value) #uncomment to verify max values if needed
    max_list[i,1] = max_intensity
    max_list[i,0] = time_counter
    time_counter = time_counter+Delay_time_step
np.savetxt('2DES_max_cumulant_GB_values.txt',max_list)
