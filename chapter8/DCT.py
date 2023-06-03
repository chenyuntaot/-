from math import cos, pi, sqrt 
import numpy as np
from skimage import data
from matplotlib import pyplot as plt 
import cv2

def dct_2d (image, numberCoefficients=0) :
    nc = numberCoefficients
    height = image.shape [0]
    width = image. shape [1]
    imageRow = np.zeros_like (image) .astype (float)
    imageCol = np.zeros_like (image) .astype (float)
    for h in range (height):
        imageRow[h,:] = dct_1d(image [h, :], nc)
    for w in range (width):
        imageCol[:, w] = dct_1d(imageRow[:, w], nc)
    return imageCol

def dct_1d (image, numberCoefficients=0):
    nc = numberCoefficients
    n = len(image)
    newImage = np.zeros_like (image).astype(float)
    for k in range(n) :
        sum = 0
        for i in range (n):
            sum += image[i] * cos (2 * pi * k / (2.0 * n) * i + (k * pi) / (2.0*n))
        ck = sqrt(0.5) if k==0 else 1
        newImage[k] = sqrt(2.0 / n) * ck * sum
    if nc > 0:
        newImage.sort()
        for i in range(nc, n) :
            newImage[i] = 0
    return newImage

def idct_2d(image):
    height = image.shape[0]
    width = image.shape[1]
    imageRow = np.zeros_like(image).astype(float)
    imageCol = np.zeros_like(image).astype(float)
    for h in range (height):
        imageRow[h, :] = idct_1d(image[h, :])
    for w in range (width) :
        imageCol[:, w] = idct_1d(imageRow[:, w])
    return imageCol

def idct_1d(image):
    n = len(image)
    newImage = np.zeros_like(image).astype(float)
    for i in range(n):
        sum = 0
        for k in range(n) :
            ck = sqrt(0.5) if k == 0 else 1
            sum += ck * image[k] * cos (2 *pi *k/ (2.0*n) * i + (k * pi) / (2.0 * n))
        newImage[i] = sqrt(2.0 / n) * sum
    return newImage

if __name__ =='__main__':
    image=cv2.imread(r"C:\Users\23282\Desktop\PYL\DIP\imageset\rose479by512.tif",0)
    numberCoefficients=10
    imgResult = dct_2d(image, numberCoefficients)
    idct_img = idct_2d(imgResult)

    plt.subplot (1, 3, 1),plt.imshow (image)
    plt.subplot (1, 3, 2),plt.imshow (imgResult) 
    plt.subplot (1, 3, 3),plt.imshow (idct_img)
    plt.show ()