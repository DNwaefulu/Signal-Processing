# -*- coding: utf-8 -*-
"""
Deion Nwaefulu
CSE 3313
1001226334
"""

import csv
import numpy as np

def bit(initial):
    initial = initial/np.linalg.norm(initial)
    pulse0 = np.ones(10)
    pulse0 = pulse0/np.linalg.norm(pulse0)
        
    pulse1 = np.append(np.ones(5), -1 * np.ones(5))
    pulse1 = pulse1/np.linalg.norm(pulse1)
        
    equal0 = np.abs(np.dot(pulse0, initial))
    equal1 = np.abs(np.dot(pulse1, initial))
        
    if equal0 > equal1:
        return '0'
        
    elif equal0 < equal1:
        return '1'
        
initial = np.ones(10) #Displays 10 pulse values
binary = ""  #Place to store 8bits of binary numbers
letter = ""  #Store the letters from the ASCII characters
 
j = 0       
i = 0

with open('data-communications.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for asc in csv_reader:
        line = asc
    
    for bin in line:
        initial[i] = bin
        i+= 1
        if i == 10:                 #A full 10 from csv
            binary+= bit(initial)   #Add binary value
            j+= 1
            i = 0
            if j == 8:
                letter+= chr(int(binary, 2))    #Convert to ASCII
                binary = ""                     #Clear string
                j = 0
                
print(letter)