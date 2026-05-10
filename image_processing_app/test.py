import cv2 as cv
import matplotlib.pyplot as plt
from processors.edges import laplacian, sobel, canny
from processors.transforms import translation
img = cv.imread('/home/favourty/Documents/Computer_vision_journey/image_processing_app/assets/favour.jpg')

lap = laplacian(img)
sob = sobel(img)
can = canny(img)
trans = translation(img)

#plt.subplot(1,3,1), plt.imshow(lap, cmap='gray'), plt.title('Laplacian')
#plt.subplot(1,3,2), plt.imshow(sob, cmap='gray'), plt.title('Sobel')
#plt.subplot(1,3,3), plt.imshow(trans), plt.title('Translation')
#plt.show()
plt.imshow(trans)
plt.show()