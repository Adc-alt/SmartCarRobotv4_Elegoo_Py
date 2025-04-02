"""
Obstacle Avoidance Application
-----------------------------

This application implements autonomous obstacle avoidance for the ELEGOO Smart Robot Car.
It uses ultrasonic sensors to detect obstacles and implements a state machine to navigate
around them.

Main components:
- Ultrasonic sensor for distance measurement
- Camera for visual feedback
- MPU6050 for motion data
- State machine for navigation logic

Usage:
    python -m apps.obstacle_avoidance.main
"""

from src.myCar import myCar
from src.camera import Camera
from src.mpuPlot import mpuPlot
from src.obstacleAvoidance import obstacleAvoidance, States

__version__ = "1.0.0"
__author__ = "Your Name"

# Export main classes
__all__ = ['myCar', 'Camera', 'mpuPlot', 'obstacleAvoidance', 'States']
