import json
import sys
import os
import time
import RPi.GPIO as GPIO

INCHES_PER_ROTATION = 4 #1.9625
STEPS_PER_ROTATION = 400
WINDOW_HIEGHT = 40 #in inches
SPEED = 5

# -1 open
# 1 close

def getId():
    return 1

def calcSteps():
  rot = WINDOW_HIEGHT / INCHES_PER_ROTATION
  return rot * STEPS_PER_ROTATION

def update(state):
    try:
        DISTANCE = 40

        GPIO.setmode(GPIO.BCM)
        StepPins = [15,18,14,23]

        for pin in StepPins:
            print "Setup pins"
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, False)

        Seq = [[1,0,0,1],
               [1,0,0,0],
               [1,1,0,0],
               [0,1,0,0],
               [0,1,1,0],
               [0,0,1,0],
               [0,0,1,1],
               [0,0,0,1]]

        if state == 1:
            StepDir = 1
        else:
            StepDir = -1

        StepCount = len(Seq)
        WaitTime = int(SPEED)/float(1000)
        StepCounter = 0
        count = 0
        rotation = calcSteps()

        while count != rotation:
            for pin in range(0,4):
                xpin=StepPins[pin]
                if Seq[StepCounter][pin]!=0:
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)

            StepCounter = StepCounter + StepDir


            if (StepCounter>=StepCount):
                StepCounter = 0
            if (StepCounter<0):
                StepCounter = StepCount+StepDir

            time.sleep(WaitTime)
            count = count + 1

        return True

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

    return True
