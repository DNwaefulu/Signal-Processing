import numpy as np
import matplotlib.pyplot as plt

def xn(n, x):
    if n < 0 or n > len(x) - 1:
        return 0
    return x[n]

def yn(n, w, y, x):
    if n < 0:
        return 0
    if n < len(x - 1):
        return x[n]
    
    equation = 1.8744 * np.cos(w) * yn(n - 1, w, y, x) - 0.8783 * yn(n - 2, w, y, x) + xn(n, y) - 2 * np.cos(w) * xn(n - 1, y) + xn(n - 2, y)
    return equation

def applyNotch(fs, dataFile) :
    y = np.loadtxt(dataFile,
               unpack = True,
               delimiter = ',')
    x = np.array([])
    f = 17
    w = (2 * np.pi * f)/fs #Normalized radian frequency
    for n in range(0, len(y) + 100):
        x = np.append(x, yn(n, w, y, x))
    
    plt.figure(1)
    plt.plot(y)
    plt.xlim(-25, 625)
    plt.title("X-axis Original Signal")
    
    plt.figure(2)
    plt.plot(x)
    plt.ylim(-2.25, 2.25)
    plt.title("Y-axis Filtered Signal")
    
    plt.figure(3)
    x = np.arange(fs)
    result1 = np.sin(2 * np.pi * 10 * x / fs)
    result2 = np.sin(2 * np.pi * 33 * x / fs)
    result = result1 + result2
    plt.plot(result)
    plt.xlim(-25, 625)
    plt.title("Combined Signal")
    plt.show()


############################################################
###########################  main  #########################
if __name__ == "__main__":
    fs = 500
    dataFileName = "notchData.csv"

    # write this function
    applyNotch(fs, dataFileName)
