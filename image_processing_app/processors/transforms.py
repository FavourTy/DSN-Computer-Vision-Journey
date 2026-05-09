import cv2 as cv
import numpy as np

def resize(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    resized = cv.resize(rgb, (700, 500))
    return resized
def translation(img):
    #rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    rows, cols = img.shape[:2]
    pt1 = np.float32([[500,6000],[500, 1000], [8000, 6000]])
    pt2 = np.float32([[500, 4500], [3000, 1500], [5000, 6000]])
    M = cv.getAffineTransform(pt1, pt2)
    dst = cv.warpAffine(img, M, (cols, rows))
    final = cv.resize (dst, (700, 500))
    return final

