"""
Deion Nwaefulu
CSE 3313
1001226334
"""

import numpy as np
import soundfile as sf
from scipy import signal
from sklearn.decomposition import FastICA, PCA
import matplotlib.pyplot as plt


def unmixAudio(leftName, rightName) :
    wave1, fsample1 = sf.read(leftName)
    wave2, fsample2 = sf.read(rightName)
    
    S = np.c_[wave1, wave2]
    
    ica = FastICA(n_components=2, random_state = 0)
    S_ = ica.fit_transform(S)
    
    result1 = S_[:, 0]
    result1 = np.multiply(result1, 10)
    result2 = S_[:, 1]
    result2 = np.multiply(result2, 10)
    
    sf.write("unmixed0.wav", result1, fsample1)
    sf.write("unmixed1.wav", result2, fsample2)
    
    plt.figure(1)
    plt.subplot(4, 1, 1)
    plt.plot(wave1)
    plt.title("darinSiren0.wav")
    
    plt.figure(2)
    plt.subplot(4, 1, 2)
    plt.plot(wave2)
    plt.title("darinSiren1.wav")
    
    plt.figure(3)
    plt.subplot(4, 1, 3)
    plt.plot(result1)
    plt.title("unmixed0.wav")
    
    plt.figure(4)
    plt.subplot(4, 1, 4)
    plt.plot(result2)
    plt.title("unmixed1.wav")


###################  main  ###################
if __name__ == "__main__" :
    leftName = "darinSiren0.wav"
    rightName = "darinSiren1.wav"
    unmixAudio(leftName, rightName)
