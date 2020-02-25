"""
Deion Nwaefulu
CSE 3313
1001226334
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
import soundfile as sf
from scipy.signal import spectrogram
import glob

def Normal(s, t):
    return np.linalg.norm(s - t, 1)
    
def PlotSpectrogram(wave, fsample):
    plt.specgram(wave, Fs=fsample)
    plt.show()

def classifyMusic() :
    songList = glob.glob("song-*.wav")
    signatureTable = {}
    song = []
    
    #Goes through the names and signatures for the songs
    for names in songList:
        wave, fsample = sf.read(names)
        signatureTable[names] = wave
        f, t, Sxx = spectrogram(wave, fsample, nperseg=fsample//2)
        for x in range(0, len(Sxx[0])):
            signature = np.array([])
            signature = np.append(signature, f[np.argmax(Sxx[:, x])])
        signatureTable[names] = signature
    
    #Retrieve the signature from a test song    
    wave1, fsample1 = sf.read("testSong.wav")
    f, t, Sxx = spectrogram(wave1, fsample1, nperseg=fsample1//2)
    testSignature = np.array([])
    for y in range(0, len(Sxx[0])):
        testSignature = np.append(testSignature, f[np.argmax(Sxx[:, y])])
        
    for z in signatureTable:
        norm = Normal(signatureTable[z], testSignature)
        song.append([norm, z])
        
    song = sorted(song, key=lambda x: x[0])
    
    for list in song[:5]:
        print('{0:.0f}  {1}'.format(list[0], list[1]))
    
    plt.figure()
    plt.title("Test Song")
    PlotSpectrogram(wave1, fsample1)
    
    #First Match
    plt.figure()
    plt.title("First Match")
    wave, fsample = sf.read(song[0][1])
    PlotSpectrogram(wave, fsample)
    
    #Second Match
    plt.figure()
    plt.title("Second Match")
    wave, fsample = sf.read(song[1][1])
    PlotSpectrogram(wave, fsample)


###################  main  ###################
if __name__ == "__main__" :
    classifyMusic()
