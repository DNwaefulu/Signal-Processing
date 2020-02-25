# -*- coding: utf-8 -*-
"""
Deion Nwaefulu
CSE 3313
1001226334
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

y = np.loadtxt('data-filtering.csv',
               unpack = True,
               delimiter = ',')

################################# Lowpass Filter ##############################
#Original signal plot
x = np.arange(0, 2000, 1)
plt.figure(1)
plt.subplots_adjust(hspace = 0.75)
plt.subplot(3, 1, 1)
plt.plot(x,y)
plt.title("original signal")

#4Hz signal plotting
f1 = 4
y1 = np.cos(2*np.pi*f1*x/2000);
name2 = "%d Hz signal" % f1
plt.subplot(3, 1, 2)
plt.plot(x, y1)
plt.title(name2)

#Application of lowpass filter   
fsample = 2000
fcutoff = 50
flength = 21
M = flength - 1
ft = fcutoff/fsample
w = np.array([])

for n in range(0 , flength):
        y1 = np.sin(2 * np.pi * ft * (n - M/2))
        y2 = (np.pi * (n - M/2))
        result1 = y1/y2
        result2 = 2 * ft
        
        if n != M/2:
            w = np.append(w, result1)
        else:
            w = np.append(w, result2)
            
lowpass = np.convolve(w, y)
plt.subplot(3, 1, 3)
plt.plot(lowpass)
plt.title("application of lowpass filter")

############################## Highpass Filter ################################
#Original signal plot
x = np.arange(0, 100, 1)
yhigh = y[0:100]
plt.figure(2)
plt.subplots_adjust(hspace = 0.75)
plt.subplot(3, 1, 1)
plt.plot(yhigh)
plt.title("original signal")

#330Hz signal plotting
f1 = 330
y1 = np.cos(2*np.pi*f1*x/fsample);
name5 = "%d Hz signal" % f1
plt.subplot(3, 1, 2)
plt.plot(x, y1)
plt.title(name5)

#Application of highpass filter   
fcutoff_high = 280
ft_high = fcutoff_high/fsample
w_high = np.array([])

for n in range(0 , flength):
        y3 = (-1 * np.sin(2 * np.pi * ft_high * (n - (M/2))))
        y4 = (np.pi * (n - M/2))
        result3 = y3/y4
        result4 = (1 - (2 * ft_high))
        
        if n != M/2:
            w_high = np.append(w_high, result3)
        else:
            w_high = np.append(w_high, result4)
            
highpass = np.convolve(w_high, yhigh)
plt.subplot(3, 1, 3)
plt.plot(highpass)
plt.title("application of highpass filter")