from src.mpu_plot import MPUPlotter
import time

def main():
    # Create plotter instance
    plotter = MPUPlotter()
    
    try:
        print("Window opened. Close it to exit.")
        while plotter.is_open():
            time.sleep(0.1)  # Small delay
                
        plotter.cleanup()
        
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        plotter.cleanup()

if __name__ == "__main__":
    main()

