# -*- coding: utf-8 -*-
"""
Deion Nwaefulu
CSE 3313
1001226334
"""
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

data, fsample = sf.read('P_9_2.wav')

fcutoff = 7500
flength = 101
M = flength - 1
ft = fcutoff/fsample

#Hamming window
weight = np.array([])

for n in range(0, flength):
    window1 = np.cos((2*np.pi*n)/M)
    window2 = 0.54 - 0.46*window1
    
    weight = np.append(weight, window2)

#Application of lowpass filter   
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

#Application of frequency response           
x, y = freqz(w, 1)
plt.plot(x, abs(y))

cross = np.multiply(w, weight)

x, y = freqz(cross, 1)
plt.plot(x, abs(y))

plt.title("Frequency Response")
plt.legend(["original","windowed"])

sound = np.convolve(cross, data)
sf.write('cleanMusic.wav', sound, fsample)