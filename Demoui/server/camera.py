import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
    def getLiveSketch(self):
        success, image = self.video.read()
        def draw(img):
            img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
            Blur_img = cv2.GaussianBlur(img_gray, (5,5), 0)
            # edges
            canny_edges = cv2.Canny(img,70,200)
            ret, mask = cv2.threshold(canny_edges,  80, 255,cv2.THRESH_BINARY_INV)
            return mask
        ret,jpeg = cv2.imencode('.jpg', draw(image))
        return jpeg.tobytes()