#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Teusday Apr 5 15:17:00 2022

@author: Sapana Shedge
"""


import numpy as np
import sys

x =  float(sys.argv[2])/27.21
y =  float(sys.argv[3])/27.21
dl = 0.06/27.21
filename = sys.argv[1].split('_')[:-1]
#print(filename)
#line="2.78 2.78"

def is_in_square(omega_3,omega_1) :
    bl_x = x - dl  # bottom left x
    bl_y = y - dl  # bottom left y
    tr_x = x + dl  # top right x
    tr_y = y + dl  # top right y
    bl = [bl_x, bl_y]
    tr = [tr_x, tr_y]
    if (omega_3 > bl[0] and omega_3 < tr[0] and omega_1 > bl[1] and omega_1 < tr[1]) :
       return True 

numbers = range(0,90)

writefileobj=open('oscillatory_'+sys.argv[2]+'_'+sys.argv[3]+'.dat','w')
writefileobj2=open('chunk.dat','w')

for snapshot in numbers:
    fullfilename = filename[0]+'_'+filename[1]+'_'+filename[2]+'_'+filename[3]+'_'+str(snapshot)+'.dat'
    fileobj = open(fullfilename,'r')
    data = fileobj.readlines()

    intensity = [] 
    for row in data:
        if len(row.strip()) != 0 :
            intensity.append(float(row.split()[2]))
            max_int=max(intensity)

    sum_inten = 0.0
    chunk = []
    for line in data:
        if len(line.strip()) != 0 :
            split_line=line.split()
            omega_3=float(split_line[0])
            omega_1=float(split_line[1])
            inten=float(split_line[2])
            if is_in_square(omega_3,omega_1) :
                sum_inten = sum_inten + inten
                chunk.append(inten)

    writeline=str(snapshot)+'\t'+str(sum_inten)+'\n'
    writefileobj.write(writeline)
   
    for line in chunk:
        writefileobj2.write(str(line)+'\n')





