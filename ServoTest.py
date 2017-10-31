import sys
import time
import RPi.GPIO as GPIO

servo1 = 15
dutyCycle=1.4

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


GPIO.setup(servo1,GPIO.OUT)

GPIO.output(servo1, False)

#1.6   1.4    1.18

while(1):
    location = raw_input("Enter location:")
    if (location == "1"):
        dutyCycle=1.6
    elif (location == "2"):
        dutyCycle = 1.4
    elif (location == "3"):
        dutyCycle=1.18
    #dutyCycle = float(dutyCycle)
    print(dutyCycle)
    for x in range(0,5):
        GPIO.output(servo1, True)
        time.sleep(dutyCycle/1000.0)
        GPIO.output(servo1, False)
        time.sleep((20.0-dutyCycle)/1000.0)
    time.sleep(0.1)
    for x in range(0,5):
        GPIO.output(servo1, True)
        time.sleep(dutyCycle/1000.0)
        GPIO.output(servo1, False)
        time.sleep((20.0-dutyCycle)/1000.0)
##    dutyCycle=3
##    raw_input("PressEnter")
##    for x in range(0,15):
##        GPIO.output(servo1, True)
##        time.sleep(dutyCycle/1000.0)
##        GPIO.output(servo1, False)
##        time.sleep((20.0-dutyCycle)/1000.0)
