import cv2
import numpy as np
image = cv2.imread('owl.jpg')
height, width = image.shape[:2]
rotation_Matrix = cv2.getRotationMatrix2D((width/2,height/2),45,1)
roatated_image = cv2.warpAffine(image,rotation_Matrix,(width, height))
cv2.imshow('roated Image',roatated_image)
cv2.waitKey()
cv2.destroyAllWindows()