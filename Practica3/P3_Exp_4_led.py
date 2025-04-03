import RPi.GPIO as GPIO
import threading
from time import sleep

# Desactivar advertencias
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Configurar los pines GPIO como salida y en bajo
valoresGPIOS = [12, 16, 18, 22, 26, 24, 32]
for pin in valoresGPIOS:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

# Variable compartida para la velocidad
velocidad = 0.5  # Valor inicial
lock = threading.Lock()  # Para proteger la variable

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

# Bucle principal para parpadear los LEDs
while True:
    for valor in valoresGPIOS + list(reversed(valoresGPIOS)):  
        GPIO.output(valor, GPIO.HIGH)
        with lock:
            vel = velocidad  
        sleep(vel)  
        GPIO.output(valor, GPIO.LOW)
