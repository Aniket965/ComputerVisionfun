# Scaling
import cv2
import numpy as np
image = cv2.imread('owl.jpg')

scaled_image = cv2.resize(image, None, fx = 0.75, fy = 0.75)
cv2.imshow('Scaled image ', scaled_image)
cv2.waitKey()

# Interpolated Image
img_scaled = cv2.resize(image, (900,400), interpolation = cv2.INTER_CUBIC)
cv2.imshow('interpolated image', img_scaled)

# Image Pyramids 
## Doubles a image size or decrease the Image Size by half
img_pyr_down = cv2.pyrDown(image)
cv2.imshow('Sequezed using Pyramid', img_pyr_down)

cv2.waitKey()

cv2.destroyAllWindows()