import cv2 as cv
import numpy as np


def binary(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 127,255, cv.THRESH_BINARY)
    final = thresh
    return thresh
def zero(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 127,255, cv.THRESH_TOZERO)
    final = thresh
    return thresh
def binaryInverse(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 127,255, cv.THRESH_BINARY_INV)
    final = thresh
    return thresh
def otsu(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 0, 255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    final = thresh
    return thresh
def adaptiveMean(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 11, 2)
    final = thresh
    return final
def adaptiveGaussian(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    final = thresh
    return final
