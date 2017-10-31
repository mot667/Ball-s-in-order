import pic
import Analyser
import SimpleCV as scv
import time
import RPi.GPIO as GPIO

imgPath = "./images/img.jpg"
mycam = scv.Camera()

#Config
servoPort = 15
solenoidPort = 11
dutyCycle=1.4
solenoidOpenDelay = (150/1000.0)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Setup the Ports
GPIO.setup(servoPort,GPIO.OUT)
GPIO.output(servoPort, False)
GPIO.setup(solenoidPort,GPIO.OUT)
GPIO.output(solenoidPort, True)

#Functions
def selectChute(ballType):
    if (ballType == 'wood'):
        print("HELLOOOOOO")
        global dutyCycle
        dutyCycle=1.6
    elif (ballType == "gum"):
        global dutyCycle
        dutyCycle=1.4
    elif (ballType == "marble"):
        global dutyCycle
        dutyCycle=1.18
    moveChute()

def moveChute():
    print("duty cycle is ", dutyCycle)
    for x in range(0,5):
        GPIO.output(servoPort, True)
        time.sleep(dutyCycle/1000.0)
        GPIO.output(servoPort, False)
        time.sleep((20.0-dutyCycle)/1000.0)
    time.sleep(0.1)
    for x in range(0,5):
        GPIO.output(servoPort, True)
        time.sleep(dutyCycle/1000.0)
        GPIO.output(servoPort, False)
        time.sleep((20.0-dutyCycle)/1000.0)

#Main Program Flow
raw_input("Press Enter to begin")

while(1):
    print("taking photo")
    pic.takePhoto(imgPath, mycam)

    print("Analysing")
    ballType = Analyser.getType(imgPath)

    print("Moving Chute")
    print("Ball type: ", ballType)
    selectChute(ballType)

    print("Dropping ball")
    GPIO.output(solenoidPort, False)
    time.sleep(solenoidOpenDelay)
    GPIO.output(solenoidPort, True)

    print("Loading next ball...")
    time.sleep(0.5)
