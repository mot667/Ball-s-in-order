import sys
import time
import RPi.GPIO as GPIO

servoPort = 15
solenoidPort = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Setup the Ports
GPIO.setup(servoPort,GPIO.OUT)
GPIO.output(servoPort, False)
GPIO.setup(solenoidPort,GPIO.OUT)
GPIO.output(solenoidPort, False)
