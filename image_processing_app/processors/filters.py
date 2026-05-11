import cv2 as cv
import numpy as np


def blur(img, k=15):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return cv.blur(rgb, (k, k))

def gaussianBlur(img, k=15):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return cv.GaussianBlur(rgb, (k, k), 0)

def medianBlur(img, k=15):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return cv.medianBlur(rgb, k)
def kernel(img):
    my_kernel = np.ones((5,5), np.float32)/50
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    dst = cv.filter2D(rgb, -1, my_kernel)
    return dst