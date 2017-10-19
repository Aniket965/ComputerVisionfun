import cv2
import numpy as np 
image = cv2.imread('owl.jpg')
cv2.imshow('image', image)
cv2.waitKey()

# kernal
kernal_5 = np.ones((5,5), np.float32) / 25
blurred_image = cv2.filter2D(image, -1, kernal_5)
cv2.imshow('5x5 Kernal Bluring', blurred_image)

cv2.waitKey()
cv2.destroyAllWindows()

