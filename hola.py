import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup('USR0', GPIO.OUT)
GPIO.setup('USR1', GPIO.OUT)
GPIO.setup('USR2', GPIO.OUT)
GPIO.setup('USR3', GPIO.OUT)

a = 0
while True:
    time.sleep(1)
    if(a == 0):
        GPIO.output('USR0', GPIO.HIGH)
        GPIO.output('USR1', GPIO.HIGH)
        GPIO.output('USR2', GPIO.HIGH)
        GPIO.output('USR3', GPIO.HIGH)
        a = 1
    else:
        GPIO.output('USR0', GPIO.LOW)
        GPIO.output('USR1', GPIO.LOW)
        GPIO.output('USR2', GPIO.LOW)
        GPIO.output('USR3', GPIO.LOW)
        a = 0
