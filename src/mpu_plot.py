import matplotlib.pyplot as plt
import numpy as np

class MPUPlotter:
    def __init__(self):
        # Create a resizable window
        plt.ion()  # Enable interactive mode
        self.fig = plt.figure(figsize=(10, 6))
        self.fig.canvas.manager.set_window_title('MPU Data')
        plt.grid(True)
        
    def is_open(self):
        return plt.fignum_exists(self.fig.number)
        
    def cleanup(self):
        plt.close(self.fig)
