import Adafruit_BBIO.GPIO as GPIO
import time

#pins
dig_out_pin = "P9_12"
GPIO.setup(dig_out_pin, GPIO.OUT)

for ii in range(0,5):
    GPIO.output(dig_out_pin, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(dig_out_pin, GPIO.LOW)
    time.sleep(5)

GPIO.cleanup()
