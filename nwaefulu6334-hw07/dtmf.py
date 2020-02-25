"""""
Deion Nwaefulu
CSE 3323
1001226334
"""""
from scipy.signal import freqz
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import csv

def keypad(column, row):
    if column is 0 and row is 4:
        return '1'
    elif column is 1 and row is 4:
        return '4'
    elif column is 2 and row is 4:
        return '7'
    elif column is 3 and row is 4:
        return '*'
    elif column is 0 and row is 5:
        return '2'
    elif column is 1 and row is 5:
        return '5'
    elif column is 2 and row is 5:
        return '8'
    elif column is 3 and row is 5:
        return '0'
    elif column is 0 and row is 6:
        return '3'
    elif column is 1 and row is 6:
        return '6'
    elif column is 2 and row is 6:
        return '9'
    elif column is 3 and row is 6:
        return '#'

def BandPassFilter(L, fs, samplesPerTone, tone):
    frequencies = np.array([697, 770, 852, 941, 1209, 1336, 1477])
    values = np.array([])
    for x in range(0, len(frequencies)):
        n = np.arange(0, L, 1)
        h = np.array([])
        for y in range(0, L):
            h = np.append(h, 2/L * np.cos(2 * np.pi * frequencies[x] * n[y] / fs))
        y = np.convolve(tone, h)
        values = np.append(values, np.mean(y ** 2))
    
    #Utilizes the Wagner coding theorem
    #The first two store values from the for loop
    max1 = 0
    max2 = 0
    
    #Last two store values from the for loop and puts them into the keypad function
    max3 = 0
    max4 = 0
    
    for z in range(0, len(values)):
        if values[z] > max1:
            max2 = max1
            max4 = max3
            max1 = values[z]
            max3 = z
        elif max1 > values[z] > max2:
            max2 = values[z]
            max4 = z
    
    #For the numbers to go into
    maxtemp = 0
    if max4 > max3:
        maxtemp = max3
        max3 = max4
        max4 = maxtemp
    return str(keypad(int(max4), int(max3)))

def processTones(name, L, fs, samplesPerTone) :
    y = np.loadtxt(name, unpack = True, delimiter = ',')
    number = ' '
    x = 0
    while x < len(y):
        data = y[x:x + 3999]
        number = number + str(BandPassFilter(L, fs, samplesPerTone, data))
        x = x + 4000
        
    frequencies = np.array([697, 770, 852, 941, 1209, 1336, 1477])
    plt.figure(1)
    plt.title("Frequency Responses of Bandpass Filters")
    plt.xlabel("Hertz")
    for x in range(0, len(frequencies)):
        n = np.arange(0, L, 1)
        h = np.array([])
        for z in range(0, L):
            h = np.append(h, 2/L * np.cos(2 * np.pi * frequencies[x] * n[z] / fs))
        a, b = freqz(h, 1)
        plt.plot(a * 1000, abs(b))
    plt.figure(2)
    f, t, Sxx = signal.spectrogram(y, fs)
    plt.pcolormesh(t, np.fft.fftshift(f), np.fft.fftshift(Sxx, axes=0))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()
    return number

#############  main  #############
if __name__ == "__main__":
    filename = "tones.csv"  #  name of file to process
    L = 64                  #  filter length
    fs = 8000               #  sampling rate
    samplesPerTone = 4000   #  4000 samples per tone, 
                            #    NOT the total number of samples per signal

    # returns string of telephone buttons corresponding to tones
    phoneNumber = processTones(filename, L, fs, samplesPerTone)
    
    print(phoneNumber)
