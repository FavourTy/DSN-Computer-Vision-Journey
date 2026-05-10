import cv2 as cv
import numpy as np

def resize(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    resized = cv.resize(rgb, (700, 500))
    return resized
def translation(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    rows, cols = rgb.shape[:2]
    
    M = np.float32([[1, 0, 100],[0,1,50]])
    dst = cv.warpAffine(rgb, M, (cols, rows))
    final = cv.resize (dst, (700, 500))
    return final

