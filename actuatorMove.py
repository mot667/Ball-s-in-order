import sys
import time
import RPi.GPIO as GPIO

pin = 11
delay = (150/1000.0)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin, False)
input=""

##while(input != "exit"):
##    GPIO.output(pin, True)
##    print("press enter to turn off")
##    input = raw_input()
##    GPIO.output(pin, False)
##    print("press enter to turn on")
##    input = raw_input()

GPIO.output(pin, True)

while(input != "exit"):
    input = raw_input("enter")
    GPIO.output(pin, False)
    time.sleep(delay)
    GPIO.output(pin, True)

GPIO.output(pin, False)
print("done")
    


