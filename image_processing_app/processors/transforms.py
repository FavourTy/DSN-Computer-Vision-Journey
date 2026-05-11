import cv2 as cv
import numpy as np

def resize(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    resized = cv.resize(rgb, (700, 500))
    return resized

def translation(img, shift_x=100, shift_y=50):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    rows, cols = rgb.shape[:2]
    M = np.float32([[1, 0, shift_x],
                    [0, 1, shift_y]])
    dst = cv.warpAffine(rgb, M, (cols, rows))
    return dst

def shear(img, shear_factor=0.3):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    rows, cols = rgb.shape[:2]
    M = np.float32([[1, shear_factor, 0],
                    [0, 1,            0]])
    new_cols = int(cols + rows * shear_factor)
    dst = cv.warpAffine(rgb, M, (new_cols, rows))
    return dst

def rotation(img, angle=45):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    rows, cols = rgb.shape[:2]
    M = cv.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    dst = cv.warpAffine(rgb, M, (cols, rows))
    return dst

def perspective_transform(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    rows, cols = rgb.shape[:2]
    pts1 = np.float32([[0, 0], [cols, 0],
                        [0, rows], [cols, rows]])
    pts2 = np.float32([[50, 0], [cols - 50, 0],
                        [0, rows], [cols, rows]])
    M = cv.getPerspectiveTransform(pts1, pts2)
    dst = cv.warpPerspective(rgb, M, (cols, rows))
    return dst

def affine_transform(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    rows, cols = rgb.shape[:2]
    pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
    pts2 = np.float32([[cols * 0.1, rows * 0.1],
                        [cols - 1, rows * 0.1],
                        [cols * 0.1, rows - 1]])
    M = cv.getAffineTransform(pts1, pts2)
    dst = cv.warpAffine(rgb, M, (cols, rows))
    return dst