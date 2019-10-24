import Adafruit_BBIO.GPIO as GPIO
import time
import pickle

recep_input = "P9_11"
GPIO.setup(recep_input, GPIO.IN)

detections = []

try:
    while(True):
        if GPIO.input(recep_input):
            detections.append(0)
        else:
            detections.append(1)
        time.sleep(0.02)

except KeyboardInterrupt:
    with open("laser_data.pickle" , "wb") as handle:
        pickle.dump(detections, handle)
    GPIO.cleanup()
