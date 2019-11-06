import Adafruit_BBIO.GPIO as GPIO
import time
import pickle

recep_power = "P9_13"
recep_input = "P9_11"
GPIO.setup(recep_power, GPIO.OUT)
GPIO.setup(recep_input, GPIO.IN)

talanquera_power = "P9_22"
talanquera_input = "P9_21"
GPIO.setup(talanquera_power, GPIO.OUT)
GPIO.setuo(talanquera_input, GPIO.IN)

detections = {}

GPIO.output(recep_power, GPIO.HIGH)
GPIO.output(talanquera_power, GPIO.HIGH)

try:    
    while(True):   
        ii = 0
        detections[ii] = []
        if GPIO.input(talanquera_input):
            if GPIO.input(recep_input): 
                detections[ii].append(0)
            else:
                detections[ii].append(1)
            time.sleep(0.02)
        else:
            ii+=1

except KeyboardInterrupt:
    GPIO.output(recep_power, GPIO.LOW)
    with open("laser_data.pickle" , "wb") as handle:
        pickle.dump(detections, handle)
    GPIO.cleanup()
