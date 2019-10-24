import Adafruit_BBIO.GPIO as GPIO
import time

out_pin = "P9_12" #pin reference
GPIO.setup(out_pin, GPIO.OUT)

l = [0,1,0,0]
u = [0,0,1]
i = [0,0]
s = [0,0,0]
a = [0,1]

LUISA = [l, u, i, s, a]

for letra in LUISA:
    for ii in range(len(letra)):

        if letra[ii] = 0:
            GPIO.output(out_pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(dig_out_pin, GPIO.LOW)
            time.sleep(1)
        else:
            GPIO.output(out_pin, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(dig_out_pin, GPIO.LOW)
            time.sleep(1)

    time.sleep(3)

GPIO.cleanup()
