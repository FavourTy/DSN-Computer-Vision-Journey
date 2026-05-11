import cv2 as cv
import numpy as np

def watershedSegment(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    _, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
    opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)
    
    sure_bg = cv.dilate(opening, kernel, iterations=2)
    
    dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
    _, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    
    unknown = cv.subtract(sure_bg, sure_fg)
    _, markers = cv.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv.watershed(img, markers)
    img[markers == -1] = [0, 0, 255] 
    return cv.cvtColor(img, cv.COLOR_BGR2RGB)