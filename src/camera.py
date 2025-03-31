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
            print(f"Error: {str(e)}")
            return None

    def show_image(self, img):
        cv2.imshow('Camera', img)
            
    def cleanup(self):
        try:
            cv2.destroyAllWindows()
        except:
            pass
            
    def run(self):
        """Main loop to show camera feed"""
        try:
            print("Starting camera feed... Press 'q' to quit")
            while True:
                # Capture and show image
                img = self.capture()
                
                # Check if window was closed
                if cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) < 1:
                    break
                
                # Show frame
                self.show_image(img)
                
                # Check for 'q' key to quit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        except Exception as e:
            print(f"\nError occurred: {str(e)}")
        finally:
            self.cleanup() 