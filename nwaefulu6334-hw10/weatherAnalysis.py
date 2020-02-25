"""
Deion Nwaefulu
CSE 3313
1001226334
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

def getData(fn) :
    fields = [] 
    rows = []
    temp = []
      
    # reading csv file 
    with open(fn, 'r') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
          
        # extracting field names through first row 
        fields = next(csvreader)
      
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
      
    for row in rows: 
        content = list(row[i] for i in [12])
        f = [float(s) for s in content]
        temp = np.append(temp, f)
    tempN = len(temp)
    return temp, tempN

def analysis(temps, tfft, N) :
    #freqs = np.fft.fftfreq(len(tfft))
    #print(tfft)
    mag = np.abs(tfft)
    
    sampling = 24
    print("Sampling rate:", sampling, "samples/day")
    
    frequency = (N/sampling)
    print("Fundamental frequency:", frequency, "Hz")
    
    top = np.argpartition(-mag, 3)[:3]
    print("Largest:", top[0], "The results tell us that it is the highest in Farenheight")
    print("2nd Largest:", top[1], "The results tell us that it is constant")
    print("3rd Largest:", top[2], "The results tell us that it is lowest in Farenheight")
    
    
def plotTemps(t, tfft, N) :
    
    plt.figure(1)
    plt.plot(t[:24])
    plt.xlabel("Hours")
    plt.title("24 hours")
    
    b = np.linspace(0, 7, 24*7)
    plt.figure(2)
    plt.plot(b,t[:24*7])
    plt.xlabel("Days")
    plt.title("7 days")
    
    a = np.linspace(0, 365, 24*365-1)
    plt.figure(3)
    plt.plot(a,t[:24*365])
    plt.xlabel("Days")
    plt.title("365 days")
    
    m = np.abs(tfft[:len(tfft) // 2])
    plt.figure(4)
    plt.plot(m)
    plt.xlabel("Magnitude")
    plt.title("Magnitude")
    
    plt.figure(5)
    plt.semilogy(m)
    plt.xlabel("Log")
    plt.title("Log")
    

##################  main  ##################
#   DO NOT CHANGE THIS
fn = "weather.csv"

#  temps = list or ndarray of temperature values
#      N = number of elements in temps
temps, N = getData(fn)

#  tfft = DFT coefficents of temps
tfft = np.fft.fft(temps)

analysis(temps, tfft, N)
plotTemps(temps, tfft, N)
