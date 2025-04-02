# 🚗 Smart Car Robot v4 - Elegoo Python Implementation 🤖

## English 🇬🇧

### Important Notice ⚠️
This code is specifically designed for the [ELEGOO Smart Robot Car Kit V4.0](https://eu.elegoo.com/products/elegoo-smart-robot-car-kit-v-4-0). Before using this Python implementation, you must:

1. 📥 Download and install the official ELEGOO firmware:
   - ATmega328P firmware for motor control and sensors
   - ESP32 firmware for WiFi communication and camera
2. 📚 Review ELEGOO's original documentation and code
3. ✅ Verify that both microcontrollers are properly programmed
4. 🔍 Test basic functionality using ELEGOO's app

Without the proper microcontroller setup, this Python implementation will not work!

### Hardware Specifications 🔧
- 🧠 **Main Controller**: ATmega328P
- 📡 **WiFi Module**: ESP32-WROOM with OV2640 camera
- 🔌 **Communication**: UART/WiFi
- 📸 **Camera**: OV2640
- 🔋 **Power**: 7.4V Lithium battery pack (2 hours runtime)
- 🎯 **Sensors**: Infrared tracking, Ultrasonic distance
- 🛠️ **Motors**: DC Motors with 1:48 gear ratio

### Communication Flow 🔄
```
[Python Program] ⬅️➡️ WiFi ⬅️➡️ [Smart Car Robot]
     📱            commands        🤖
     │            data            │
     │            images          │
     │                           │
     └── Serial port ──────────► [Arduino IDE]
         (debugging only)
```

The system operates through two main communication channels:
- 📡 **WiFi Communication**: Primary channel for:
  - 🎮 Sending commands to the robot
  - 📊 Receiving sensor data (MPU)
  - 📸 Receiving camera images
  - 🌐 Default IP: 192.168.4.1

- 🔌 **Serial Port**: Secondary channel used only for debugging purposes with Arduino IDE

### Project Structure 📁
```
CameraPython/
├── main.py              # 🎯 Main entry point
├── src/
│   ├── myCar.py        # 🚙 Core car control class
│   ├── obstacleAvoidance.py  # 🛡️ Obstacle avoidance logic
│   ├── camera.py       # 📸 Camera feed handling
│   ├── mpuPlot.py      # 📊 Motion data visualization
│   ├── connection.py   # 🔌 Network communication
│   └── robotCommands.py # ⚙️ Command definitions
```

### Dependencies 📦
- Python 3.x 🐍
- OpenCV (cv2) 👁️
- NumPy 🔢
- Matplotlib 📈
- Socket (built-in) 🔌

### Key Features ✨
- 📸 Real-time camera feed
- 📊 Motion data visualization (MPU6050)
- 🛡️ Autonomous obstacle avoidance
- 🌐 Network-based control
- 🔄 Resizable camera window

### How to Run 🚀
1. 🔌 Connect to the car's WiFi network
2. 📦 Install dependencies: `pip install -r requirements.txt`
3. ▶️ Run the program: `python main.py`

### Controls 🎮
- 🤖 The car operates autonomously
- 🔄 Camera window can be resized
- 📊 Motion data is displayed in real-time
- ⏹️ Press Ctrl+C to stop the program

---

## Español 🇪🇸

### Aviso Importante ⚠️
Este código está diseñado específicamente para el [ELEGOO Smart Robot Car Kit V4.0](https://eu.elegoo.com/products/elegoo-smart-robot-car-kit-v-4-0). Antes de usar esta implementación en Python, debes:

1. 📥 Descargar e instalar el firmware oficial de ELEGOO:
   - Firmware del ATmega328P para control de motores y sensores
   - Firmware del ESP32 para comunicación WiFi y cámara
2. 📚 Revisar la documentación y código original de ELEGOO
3. ✅ Verificar que ambos microcontroladores estén correctamente programados
4. 🔍 Probar la funcionalidad básica usando la app de ELEGOO

¡Sin la configuración adecuada de los microcontroladores, esta implementación en Python no funcionará!

### Especificaciones del Hardware 🔧
- 🧠 **Controlador Principal**: ATmega328P
- 📡 **Módulo WiFi**: ESP32-WROOM con cámara OV2640
- 🔌 **Comunicación**: UART/WiFi
- 📸 **Cámara**: OV2640
- 🔋 **Alimentación**: Batería de litio de 7.4V (2 horas de autonomía)
- 🎯 **Sensores**: Seguimiento infrarrojo, Distancia ultrasónica
- 🛠️ **Motores**: Motores DC con relación 1:48

### Flujo de Comunicación 🔄
```
[Programa Python] ⬅️➡️ WiFi ⬅️➡️ [Robot Smart Car]
      📱           comandos        🤖
      │           datos           │
      │           imágenes        │
      │                          │
      └── Puerto Serial ───────► [Arduino IDE]
          (solo depuración)
```

El sistema opera a través de dos canales principales de comunicación:
- 📡 **Comunicación WiFi**: Canal principal para:
  - 🎮 Enviar comandos al robot
  - 📊 Recibir datos de sensores (MPU)
  - 📸 Recibir imágenes de la cámara
  - 🌐 IP predeterminada: 192.168.4.1

- 🔌 **Puerto Serial**: Canal secundario usado solo para propósitos de depuración con Arduino IDE

### Estructura del Proyecto 📁
```
CameraPython/
├── main.py              # 🎯 Punto de entrada principal
├── src/
│   ├── myCar.py        # 🚙 Clase principal de control del carro
│   ├── obstacleAvoidance.py  # 🛡️ Lógica de evasión de obstáculos
│   ├── camera.py       # 📸 Manejo de la cámara
│   ├── mpuPlot.py      # 📊 Visualización de datos de movimiento
│   ├── connection.py   # 🔌 Comunicación por red
│   └── robotCommands.py # ⚙️ Definiciones de comandos
```

### Dependencias 📦
- Python 3.x 🐍
- OpenCV (cv2) 👁️
- NumPy 🔢
- Matplotlib 📈
- Socket (incluido) 🔌

### Características Principales ✨
- 📸 Transmisión en vivo de la cámara
- 📊 Visualización de datos de movimiento (MPU6050)
- 🛡️ Evasión autónoma de obstáculos
- 🌐 Control basado en red
- 🔄 Ventana de cámara redimensionable

### Cómo Ejecutar 🚀
1. 🔌 Conectarse a la red WiFi del carro
2. 📦 Instalar dependencias: `pip install -r requirements.txt`
3. ▶️ Ejecutar el programa: `python main.py`

### Controles 🎮
- 🤖 El carro opera de forma autónoma
- 🔄 La ventana de la cámara se puede redimensionar
- 📊 Los datos de movimiento se muestran en tiempo real
- ⏹️ Presionar Ctrl+C para detener el programa 

## Features

- Remote control via WiFi
- Obstacle avoidance
- Camera streaming
- Motion detection
- Ground tracking

## Installation

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
- Windows:
```bash
.venv\Scripts\activate
```
- Linux/Mac:
```bash
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in development mode:
```bash
pip install -e .
```

## Usage

Run the obstacle avoidance demo:
```bash
python apps/obstacle_avoidance/main.py
```

## Project Structure

```
CameraPython/
├── apps/                    # Aplicaciones ejecutables
│   └── obstacle_avoidance/  # Módulo específico de la aplicación
├── src/                     # Código fuente principal
│   ├── __init__.py         # Inicialización del paquete
│   ├── myCar.py            # Clase principal del carro
│   ├── camera.py           # Manejo de la cámara
│   ├── connection.py       # Manejo de conexiones
│   ├── mpuPlot.py          # Visualización MPU
│   ├── obstacleAvoidance.py # Lógica de evitación
│   └── robotCommands.py    # Comandos del robot
├── pyproject.toml          # Configuración del proyecto
├── requirements.txt        # Dependencias
└── README.md              # Documentación
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors

- [Adc-alt](https://github.com/Adc-alt) - Project maintainer 