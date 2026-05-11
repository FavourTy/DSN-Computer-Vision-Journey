import cv2 as cv
import numpy as np

def opening (img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, binary_img = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+ cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
    opening = cv.morphologyEx(binary_img, cv.MORPH_OPEN, kernel, iterations=2)
    return opening

