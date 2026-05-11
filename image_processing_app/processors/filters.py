import cv2 as cv
import numpy as np

def blur(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    final = cv.blur(rgb, (250, 250))
    return final
def medianBlur(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    final = cv.medianBlur(rgb, 341)
    return final
def gaussianBlur(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    final = cv.GaussianBlur(rgb,(251, 251), 0)
    return final
def kernel(img):
    my_kernel = np.ones((5,5), np.float32)/50
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    dst = cv.filter2D(rgb, -1, my_kernel)
    return dst