import cv2
import numpy as np
image = cv2.imread('shapes.jpg')
cv2.imshow('original Image', image)
cv2.waitKey()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,30,200)
cv2.imshow('canny egdes',edges)
cv2.waitKey()
# contours
_,contours,h = cv2.findContours(edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow('contours',edges)
cv2.waitKey()
print('number of contors is '+ str(len(contours)) )
# draw contours
# print(contours)
# third argument is which contor to draw -1 is to draw all
cv2.drawContours(image,contours,-1,(0,255,0),3)
cv2.imshow('contours',image)
cv2.waitKey()
cv2.destroyAllWindows()