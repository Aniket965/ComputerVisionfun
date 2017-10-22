import cv2
import numpy as np 
foreground_background = cv2.createBackgroundSubtractorMOG2()
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    foreground_mask = foreground_background.apply(frame)
    cv2.imshow('masked',foreground_mask)
    if cv2.waitKey(1) == 13:
        cv2.imwrite('cool.jpg',foreground_mask)

    if cv2.waitKey(1) == 27:
        break
       
cv2.destroyAllWindows()
