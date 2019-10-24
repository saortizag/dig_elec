import Adafruit_BBIO.GPIO as GPIO
import time
import pickle

recep_power = "P9_13"
recep_input = "P9_11"
GPIO.setup(recep_input, GPIO.IN)
GPIO.setup(recep_power, GPIO.OUT)

detections = []

GPIO.output(recep_power, GPIO.HIGH)
try:
    
    while(True):
    
        if GPIO.input(recep_input):
            detections.append(0)
        else:
            detections.append(1)
        time.sleep(0.02)

except KeyboardInterrupt:
    GPIO.output(recep_power, GPIO.LOW)
    with open("laser_data.pickle" , "wb") as handle:
        pickle.dump(detections, handle)
    GPIO.cleanup()
