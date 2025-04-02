import numpy as np
import cv2
from urllib.request import urlopen


class Camera:
    def __init__(self, ip="192.168.4.1"):
        self.camera_url = f'http://{ip}/capture'
        # Create a named window that can be resized
        cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)
        print(f"Connecting to camera at {ip}...")

    def capture(self):
        try:
            # Get image from camera
            cam = urlopen(self.camera_url)
            img = cam.read()
            img = np.asarray(bytearray(img), dtype='uint8')
            img = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)
            return img
        except Exception as e:
            print(f"Camera error: {str(e)}")
            return None

    def show_image(self, img):
        cv2.imshow('Camera', img)
            
    def cleanup(self):        
        cv2.destroyAllWindows()
            
    def update(self):
        """Capture and display an image, returns True if window should remain open"""
        img = self.capture()
        if img is not None:
            self.show_image(img)
            cv2.waitKey(1)
        return True
            
