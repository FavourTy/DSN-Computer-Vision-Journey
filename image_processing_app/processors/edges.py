## canny, sobel, laplacian

import cv2 as cv
import numpy as np


def canny(img, t_lower=100, t_upper=200):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, t_lower, t_upper)
    return edges

def laplacian (img):
    gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    lap = cv.Laplacian(gray, cv.CV_64F)
    lap = np.uint8(np.absolute(lap))
    return lap

def sobel(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (5,5), 0)
    sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=5)
    sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1,ksize=5)
    combined = cv.magnitude(sobelX, sobelY)
    return np.uint8(np.clip(combined, 0, 255))
   
