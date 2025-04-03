# Importa la librería de control del GPIO de la Raspberry Pi
import RPi.GPIO as GPIO
import threading

# Importa la función sleep del módulo time
from time import sleep

# Desactivar advertencias (warnings)
GPIO.setwarnings(False)
# Configurar la librería para usar el número de pin.
# Llame GPIO.setmode(GPIO.BCM) para usar el canal SOC definido por Broadcom
GPIO.setmode(GPIO.BOARD)
# Configurar el pin 32 como salida y habilitar en bajo
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)

velocidad = 0.5 
lock = threading.Lock() 

# Función para escuchar la entrada del usuario y actualizar la velocidad en tiempo real
def pedir_velocidad():
    global velocidad
    while True:
        try:
            nueva_velocidad = float(input("Digite la velocidad: "))
            with lock:
                velocidad = max(0, nueva_velocidad)  # Evita valores negativos o cero
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Crear e iniciar el hilo para capturar la velocidad en tiempo real
hilo_velocidad = threading.Thread(target=pedir_velocidad, daemon=True)
hilo_velocidad.start()

while True: # Bucle infinito
	valoresGPIOS = [12, 16, 18, 22, 26, 24, 32]
	for valor in  reversed (valoresGPIOS):
		#sleep(0.1) # Espera 500ms
		GPIO.output(valor, GPIO.HIGH) # Enciende el led
		sleep(velocidad) # Espera 500ms
		GPIO.output(valor, GPIO.LOW)
