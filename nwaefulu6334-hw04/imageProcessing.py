# -*- coding: utf-8 -*-
"""
Deion Nwaefulu
CSE 3313
1001226334
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from scipy import ndimage

h = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
c = np.array([-1, 1])

def lowpass(x, y, z):
    Low = np.empty((y,z))
    for line in x:
        result = np.convolve(h,line)
        Low = np.append(Low, [result], axis=0)
        
    plt.figure()
    plt.imshow(Low, cmap = "gray")
    return Low

def highpass(x, y, z):
    High = np.empty((y,z))
    for line in x:
        result = np.convolve(c,line)
        High = np.append(High, [result], axis=0)
        
    plt.figure()
    plt.imshow(High, cmap = "gray")
    return High

#Image of boat
boat = img.imread("boat.512.tiff")
plt.imshow(boat, cmap = "gray")
plt.title("Boat")
lowpass(boat, 0, 521)
plt.title("Boat (Lowpass Filter)")
highpass(boat, 0, 513)
plt.title("Boat (Highpass Filter)")
plt.figure()

#Image of clock
clock = img.imread("clock-5.1.12.tiff")
plt.imshow(clock, cmap = "gray")
plt.title("Clock")
lowpass(clock, 0, 265)
plt.title("Clock (Lowpass filter)")
highpass(clock, 0, 257)
plt.title("Clock (Highpass filter)")
plt.figure()

#Image of man
man = img.imread("man-5.3.01.tiff")
plt.imshow(man, cmap = "gray")
plt.title("Man")
lowpass(man, 0, 1033)
plt.title("Man (Lowpass filter)")
highpass(man, 0, 1025)
plt.title("Man (Highpass filter)")
plt.figure()

#Image of tank
tank = img.imread("tank-7.1.07.tiff")
plt.imshow(tank, cmap = "gray")
plt.title("Tank")
lowpass(tank, 0, 521)
plt.title("Tank (Lowpass filter)")
highpass(tank, 0, 513)
plt.title("Tank (Highpass filter)")
plt.figure()

# Image of Darin Brezeale
darinGrayNoise = img.imread("darinGrayNoise.jpg")
plt.imshow(darinGrayNoise, cmap = "gray")
plt.title("Darin Brezeale")
lowpass(darinGrayNoise, 0, 649)
plt.title("Darin Brezeale (Lowpass filter)")

# Use of Median
output = ndimage.median_filter(darinGrayNoise, 5)
plt.figure()
plt.imshow(output, cmap = "gray")
plt.title("Darin Brezeale (Median)")
plt.figure()

plt.show()