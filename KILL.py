import sys
import time
import RPi.GPIO as GPIO

actuatorPin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(actuatorPin,GPIO.OUT)
GPIO.output(actuatorPin, False)
