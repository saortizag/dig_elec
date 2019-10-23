import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup('USR0', GPIO.OUT)
GPIO.setup('USR1', GPIO.OUT)
GPIO.setup('USR2', GPIO.OUT)
GPIO.setup('USR3', GPIO.OUT)


l = [0,1,0,0]
u = [0,0,1]
i = [0,0]
s = [0,0,0]
a = [0,1]

LUISA = [l, u, i, s, a]

for letra in LUISA:
    for ii in range(len(letra)):

while True:
    time.sleep(0.5)
    if light == 0:
        GPIO.setup('USR0', GPIO.HIGH)
        GPIO.setup('USR1', GPIO.HIGH)
        GPIO.setup('USR2', GPIO.HIGH)
        GPIO.setup('USR3', GPIO.HIGH)
