#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thurs Feb 18  01:17 2021

@author: vinny-holiday
"""

import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy.interpolate import interp1d
from scipy.interpolate import make_interp_spline
import matplotlib.font_manager as fm
import matplotlib.lines as mlines


#infile = sys.argv[1]

fig, ax = plt.subplots(figsize=(10,10))

fname=('Omega3_slice_1.7eV_frame_0.dat')
data1 = np.loadtxt(fname)
X1 = (data1[:,0])*27.2114+1.7199999999999995
Y1 = (data1[:,1]/max(data1[:,1]))**2
X_Y_Spline = make_interp_spline(X1, Y1)
X_ = np.linspace(X1.min(), X1.max(), 500)
Y_ = X_Y_Spline(X_)
plt.plot(X_, Y_,color='blue',label="0 fs",linewidth=4.0)

fname=('Omega3_slice_1.7eV_frame_10.dat')
data2 = np.loadtxt(fname)
X2 = (data2[:,0])*27.2114+1.7199999999999995
Y2 = (data2[:,1]/max(data2[:,1]))**2
X_Y_Spline = make_interp_spline(X2, Y2)
X_ = np.linspace(X2.min(), X2.max(), 500)
Y_ = X_Y_Spline(X_)
plt.plot(X_, Y_,label='40 fs',color='magenta',linewidth=4.0)

fname=('Omega3_slice_1.7eV_frame_35.dat')
data3 = np.loadtxt(fname)
X3 = (data3[:,0])*27.2114+1.7199999999999995
Y3 = (data3[:,1]/max(data3[:,1]))**2
X_Y_Spline = make_interp_spline(X3, Y3)
X_ = np.linspace(X3.min(), X3.max(), 500)
Y_ = X_Y_Spline(X_)
plt.plot(X_, Y_,label='140 fs',color='black',linewidth=4.0)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Omega3 energy (eV)', fontsize=20)
plt.ylabel('Intensity (arb.)',fontsize=20)
#plt.title('Morse Method Comparison',fontsize=25)
plt.legend()

plt.show()
