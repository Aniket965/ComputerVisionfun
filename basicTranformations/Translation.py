import cv2
image = cv2.imread('owl.jpg')
cv2.imshow('owl', image)
# print(image.shape)
height, width = image.shape[:2]
quater_height, quater_width = height/4, width/4
T = np.float32([[1,0,quater_width],[0,1,quater_height]])
Translated_image = cv2.warpAffine(image, T, (width,height))
print(quater_height)
cv2.imshow('Tranlated Image',Translated_image)
cv2.waitKey()
cv2.destroyAllWindows()