# Importa la librería de control del GPIO de la Raspberry Pi
import RPi.GPIO as GPIO
# Importa la función sleep del módulo time
from time import sleep

# Desactivar advertencias (warnings)
GPIO.setwarnings(False)
# Configurar la librería para usar el número de pin.
# Llame GPIO.setmode(GPIO.BCM) para usar el canal SOC definido por Broadcom
GPIO.setmode(GPIO.BOARD)
# Configurar el pin 32 como salida y habilitar en bajo
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)

# El siguiente código hace parpadear el led
while True: # Bucle infinito
	sleep(0.5) # Espera 500ms
	GPIO.output(32, GPIO.HIGH) # Enciende el led
	GPIO.output(12, GPIO.HIGH) # Enciende el led
	GPIO.output(16, GPIO.HIGH) # Enciende el led
	GPIO.output(18, GPIO.HIGH) # Enciende el led
	GPIO.output(22, GPIO.HIGH) # Enciende el led
	GPIO.output(24, GPIO.HIGH) # Enciende el led
	GPIO.output(26, GPIO.HIGH) # Enciende el led
	sleep(0.5) # Espera 500ms
	GPIO.output(32, GPIO.LOW) # Apaga el led
	GPIO.output(12,GPIO.LOW) # Apaga el led
	GPIO.output(16,GPIO.LOW) # Apaga el led
	GPIO.output(18,GPIO.LOW) # Apaga el led
	GPIO.output(22,GPIO.LOW) # Apaga el led
	GPIO.output(24,GPIO.LOW) # Apaga el led
	GPIO.output(26,GPIO.LOW) # Apaga el led
