import cv2
import dlib
import numpy as np
predictor_path = "path"
predictor = dlib.shape_predictor(predictor_path)
detector = dlib.get_frontal_face_detector()


class TooManyFaces(Exception):
    pass
class NoFaces(Exception):
    pass
def get_landmarks(img):
    rects = detector(img,1)
    if len(rects) > 1:
        raise TooManyFaces
    if len(rects) == 0:
        raise NoFaces
    return numpy.matrix([[p.x,p.y] for p in predictor(img,rects[0]).parts()])
def annotate_landmarks(im,landmarks):
    im = im.copy()
    for idx,point in enumerate(landmarks):
        pos = (point[0,0],point[0,1])
        cv2.putText(im, str(idx),pos,fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,color=(0,255,0))
        cv2.circle(im,pos,3,color=(0,255,255))
    return im
image = ('lol.jpg')
landmarks = get_landmarks(image)
marked_image = annotate_landmarks(image,landmarks)
cv2.imshow('image with Features',marked_image)
cv2.waitKey()
cv2.destroyAllWindows()
