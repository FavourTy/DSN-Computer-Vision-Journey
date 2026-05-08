import cv2 as cv
import numpy as np

img = np.zeros((100, 100, 3), dtype=np.uint8)
ret, thresh = cv.threshold(img,  127, 255, cv.THRESH_BINARY)
print(f"thresh shape: {thresh.shape}")

try:
    cv.bitwise_and(img, img, mask=thresh)
except Exception as e:
    print(f"Error: {e}")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh2 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
print(f"thresh2 shape: {thresh2.shape}")

cv.bitwise_and(img, img, mask=thresh2)
print("Success with gray!")

