import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def PlotFunction(wave, y):
    FFT_wave = np.abs(np.fft.fft(wave))     #File is filtered
    FFT_Filter = np.abs(np.fft.fft(y))     #Array is filtered
    plt.figure(1)
    plt.subplot(1, 2, 1)
    plt.plot(FFT_wave)
    plt.xlim(0, len(FFT_wave)/4)
    plt.ylim(0, np.max(FFT_wave) + 100)
    plt.title("Original Signal")
    plt.xlabel("Hz")
    plt.subplot(1, 2, 2)
    plt.plot(FFT_Filter)
    plt.xlim(0, len(FFT_wave)/4)
    plt.ylim(0, np.max(FFT_wave) + 100)
    plt.title("Filtered Signal")
    plt.xlabel("Hz")
    plt.show()

def applyShelvingFilter(inName, outName, g, fc) :
    wave, fsample = sf.read(inName)
    mu = 10**(g/20)
    theta = (2 * np.pi * fc) / fsample
    g1 = 1 - (4 / (1 + mu)) * np.tan(theta/2)
    g2 = 1 + (4 / (1 + mu)) * np.tan(theta/2)
    gamma = g1/g2
    alpha = (1 - gamma) / 2
    x1 = 0
    u1 = 0
    z = np.array([])
    for x in wave:
        u = alpha * (x + x1) + gamma * u1
        x1 = x
        u1 = u
        z = np.append(z, u * (mu - 1.0) + x)
    PlotFunction(wave, z)
    sf.write(outName, z, fsample) 


##########################  main  ##########################
if __name__ == "__main__" :
    inName = "P_9_1.wav"
    gain = -10  # can be positive or negative
                # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"

    applyShelvingFilter(inName, outName, gain, cutoff)
