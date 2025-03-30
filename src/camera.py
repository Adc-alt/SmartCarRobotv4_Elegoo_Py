import numpy as np
import cv2 as cv
from urllib.request import urlopen

class Camera:
    def __init__(self, ip="192.168.4.1"):
        self.camera_url = f'http://{ip}/capture'
        # Create a named window that can be resized
        cv.namedWindow('Camera', cv.WINDOW_NORMAL)

    def capture(self):
        try:
            cam = urlopen(self.camera_url)
            img = cam.read()
            img = np.asarray(bytearray(img), dtype='uint8')
            img = cv.imdecode(img, cv.IMREAD_UNCHANGED)
            return img
        except Exception as e:
            print('Error capturing image:', str(e))
            return None

    def show_image(self, img):
        if img is not None:
            cv.imshow('Camera', img)
            
    def cleanup(self):
        cv.destroyWindow('Camera') 