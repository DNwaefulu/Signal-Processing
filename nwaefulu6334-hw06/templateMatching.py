"""
Deion Nwaefulu
CSE 3313
1001226334
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from skimage.feature import match_template

#Converting RGB to grayscale function
def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def findImage(mainImage, template) :
    #Images of ERB Building
    ERB = img.imread(mainImage)
    smallERB = img.imread(template)
    gray1 = rgb2gray(ERB)
    gray2 = rgb2gray(smallERB)
    
    plt.figure()
    plt.imshow(gray1, cmap = "gray")
    plt.figure()
    plt.imshow(gray2, cmap = "gray")
    result = match_template(gray1, gray2)
    
    #Matching rows and columns
    column = np.argmax(np.max(result, axis=1))
    row = np.argmax(np.max(result, axis=0))
    
    for x in range(row, row + int(len(gray2))):
        for y in range(column, column + int(len(gray2))):
            gray1[y, x] = 0
            
    plt.figure()
    plt.imshow(gray1, cmap = "gray")
    plt.show()
    
    #Return coordinates
    return row, column

#############  main  #############
# this function should be how your code knows the names of
#   the images to process
# it will return the coordinates of where the template best fits

if __name__ == "__main__":
    mainImage = "ERBwideColorSmall.jpg"
    template = "ERBwideTemplate.jpg"
    r, c = findImage(mainImage, template)

    print("coordinates of match = (%d, %d)" % (r, c))
