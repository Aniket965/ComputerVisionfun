import cv2
import numpy as np 
image = cv2.imread('owl.jpg')
cv2.imshow('Original', image)
kernel_sharpning = np.array(
    [-1,-1,-1,
    -1,9,-1,
    -1,-1,-1]
    )
sharped_image = cv2.filter2D(image, -1, kernel_sharpning)
cv2.imshow('sharped Image', sharped_image)
cv2.waitKey()
cv2.destroyAllWindows()
