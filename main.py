from src.camera import Camera
from src.myCar import myCar
from src.mpuPlot import mpuPlot
import time

def main():
    camera = Camera()
    car = myCar()
    if not car.connect():
        print("Failed to connect to car")
        return
        
    plotter = mpuPlot()
    
    try:
        while True:
            # Show camera
            img = camera.capture()
            if img is not None:
                camera.show_image(img)
            
            # Show MPU data
            motion_data = car.measure_motion()
            if isinstance(motion_data, list):
                if not plotter.add_data(motion_data):
                    break
                    
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        plotter.close()
        camera.cleanup()
        car.disconnect()

if __name__ == "__main__":
    main()

