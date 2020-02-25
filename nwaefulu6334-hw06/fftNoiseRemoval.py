"""
Deion Nwaefulu
CSE 3313
1001226334
"""

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def processFile(fn, offset) :
    fn, fsample = sf.read(fn)
    Filter = np.fft.fft(fn)
    midIndex = int(len(Filter)/2 - 1)
    
    for x in range(midIndex - offset - 1, midIndex + offset):
        Filter[x] = 0
        
    Inverse = np.fft.ifft(Filter)
    Inverse = Inverse.real
    
    plt.figure(1)
    plt.subplot(1, 2, 1)
    plt.plot(abs(Filter))
    plt.subplot(1, 2, 2)
    plt.plot(abs(np.fft.fft(fn)))
    plt.show()
    
    sf.write('cleanMusic.wav', Inverse, fsample)
##############  main  ##############
if __name__ == "__main__":
    filename = "P_9_2.wav"
    offset = 10000

    # this function should be how your code knows the name of
    #   the file to process and the offset to use
    processFile(filename, offset)
