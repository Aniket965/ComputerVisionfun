import cv2
import numpy as np
def draw(img):
    img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    Blur_img = cv2.GaussianBlur(img_gray, (5,5), 0)
    # edges
    canny_edges = cv2.Canny(img,70,200)
    ret, mask = cv2.threshold(canny_edges,  80, 255,cv2.THRESH_BINARY_INV)
    return mask
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('Sketching...', draw(frame))
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()
