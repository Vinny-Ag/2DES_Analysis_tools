#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 18:38:04 2022

@author: vinny-holiday
"""
import numpy as np
import sys
import math

#max freeuency of mode(s), in the case of CO ex_state = 1561.9727
infile = sys.argv[1]
data = np.genfromtxt(fname= infile)


n_frames = 90 #number of 2DES frames and time points
Ha_to_cm=219474.63
Ha_to_eV=27.211396132
kb_in_Ha=8.6173303*10.0**(-5.0)/Ha_to_eV
hbar_in_eVfs=0.6582119514
fourier_tran = np.zeros((int(data.shape[0]/2),2))
fs_to_Ha=2.418884326505*10.0**(-2.0)
time_step_2DES = 4.0
sampling_rate=(1.0/time_step_2DES)*math.pi*2.0
max_t = 400/fs_to_Ha #from input file
num_steps = 600 # from input file
decayed_data = np.zeros((data.shape[0]))
fourier_tran = np.zeros((int(data.shape[0]/2),2))

dim=data.shape[0]
tau=decay_length=500.0/fs_to_Ha
eff_decay_length=tau/time_step_2DES
sampling_rate_in_fs=1.0/(time_step_2DES/fs_to_Ha)

#two ways of calculating sample_rate
sample_rate_1=1.0/(max_t/num_steps)#*math.pi*2.0
sample_rate_2=sampling_rate_in_fs*math.pi*2.0#*hbar_in_eVfs

# subtract mean of the data
mean = float(abs(np.sum(np.real(data[:,1]))/(np.shape(data[:,0]))))
# print(mean)
data[:,1]=data[:,1]-mean

#add decay function to data
for i in range(data.shape[0]):
	decayed_data[i] = (data[i,1])-np.exp(-abs(np.real(data[i,0]))/max_t)

# calculating FT 
# freqs = np.fft.fftshift(np.fft.fftfreq(data.shape[0],d=1.0/sampling_rate))
freqs = np.fft.fftshift(np.fft.fftfreq(data.shape[0],d=1/sample_rate_1))*Ha_to_cm
temp_freq = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(decayed_data)))#*max_t/num_steps*2.0*math.pi


counter = 0.0
for i in range(fourier_tran.shape[0]):

 	fourier_tran[i,1] = abs(temp_freq[i])
 	fourier_tran[i,0] = abs(freqs[i])#+counter
 	counter= counter+1.0#fstep*2

# fourier_tran[:,0] = (-fourier_tran[:,0])

np.savetxt('FT_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[1],fourier_tran)



# n_frames = 90 #number of 2DES frames and time points
# time_step = 4 #in fs
# total_sample_time = n_frames*time_step
# #max freeuency of mode(s), in the case of CO ex_state = 1561.9727
# # convert max frequancy to  time = 21 fs
# osc_period = 21.355
# #divide total time by oscillation period

# step_length=data[1,0]-data[0,0]
# freqs = np.fft.fftfreq(data.shape[0])
# # mask = freqs > 0

# fourier_tran = np.zeros((int(data.shape[0]/2),2))

# # data[i,1] = data[i,1]*np.exp(-abs(data[i,0])/500)
# temp_freq =np.fft.fftshift(np.fft.fft(np.fft.ifftshift(data[:,1]/2)))

# counter = 0.0
# for i in range(fourier_tran.shape[0]):
# 	fourier_tran[i,1] = 2.0*abs((temp_freq[i]))
# 	fourier_tran[i,0] = freqs[i]+counter
# 	counter= counter+16.857#fstep*2
# fourier_tran[:,0] = np.flip(fourier_tran[:,0])

# # fourier_tran = fourier_tran[mask]
# np.savetxt('FT_oscillatory_spec.txt',fourier_tran)





# speed_of_light_cm = 2.998*10**10
# fs_to_sec = 1*10**(-15)
# time_range_fs = 360 # in fs units, this is the max delay-time over which energy points from 2DES are integrated, i.e. 90 2DES frames with 4fs time_steps between each frame

# hertz = 1/(time_range_fs*fs_to_sec) #units of s^-1
# frequency_range = hertz/speed_of_light_cm # units of cm^-1, this value is the frequency equivalent of your time range
# print(frequency_range)

# Fs=33355 #wavenumber of 1 fs
# f0 = 92 #wavenumber of time_range_fs value (your 2DES max delay-time)
# N = int(Fs/f0)
# fstep = Fs/N

#1.7 eV = 241.79 THz = 4.1356 fs