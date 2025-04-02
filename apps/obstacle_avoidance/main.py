import traceback
import sys

from src import myCar, obstacleAvoidance, Camera, mpuPlot

def main():
    # Inicializar componentes
    car = myCar()
    camera = Camera()
    plotter = mpuPlot()
    obstacle_avoidance = obstacleAvoidance(car=car)
    
    # Conectar al carro
    print("Conectando al carro...")
    if not car.connect():
        print("Error: No se pudo conectar al carro")
        return
    
    print("Iniciando obstacle avoidance...")
    try:
        while True:
            # Ejecutar el estado actual del obstacle avoidance
            camera.update()
            obstacle_avoidance.run()
            
            # Actualizar cámara y datos MPU para observación
            
            # motion_data = car.measure_motion()
            # if isinstance(motion_data, list):
            #     plotter.add_data(motion_data)

    finally:
        print("Limpiando recursos...")
        plotter.close()
        camera.cleanup()
        car.stop()
        car.disconnect()

if __name__ == "__main__":
    main()

