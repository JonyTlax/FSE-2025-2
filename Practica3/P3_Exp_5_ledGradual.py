# Importa la librería de control del GPIO de la Raspberry Pi
import RPi.GPIO as GPIO
# Importa la función sleep del módulo time
from time import sleep

# Desactivar advertencias (warnings)
GPIO.setwarnings(False)
# Configurar la librería para usar el número de pin.
GPIO.setmode(GPIO.BOARD)
# Configurar el pin 32 como salida y habilitar en bajo
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
# Inicializar el pin 32 como PWM a una frecuencia de 2Hz
pwm = GPIO.PWM(32, 100)
# El siguiente código hace parpadear el led
pwm.start(0)

#flag = True
try:
	while True:
		for duty_cycle in range(0, 101, 1):
			pwm.ChangeDutyCycle(duty_cycle)
			sleep(0.01)
		sleep(0.5)
		for duty_cycle in range(100, -1, -1):
			pwm.ChangeDutyCycle(duty_cycle)
			sleep(0.01)
except KeyboardInterrupt:
	pass
# Detiene el PWM
pwm.stop()
# Reinicia los puertos GPIO (cambian de salida a entrada)
GPIO.cleanup()
