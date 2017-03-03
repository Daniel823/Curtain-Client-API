import json
import sys
import time
import RPi.GPIO as GPIO

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

StepCount = len(Seq)
StepDir = 1

# Initialise variables
StepCounter = 0

counter = 0
run = True
# Start main loop
while run:

  print StepCounter,
  print Seq[StepCounter]

  for pin in range(0,4):
    xpin=StepPins[pin]# Get GPIO
    if Seq[StepCounter][pin]!=0:
      print " Enable GPIO %i" %(xpin)
      GPIO.output(xpin, True)
    else:
      GPIO.output(xpin, False)

  StepCounter += StepDir
  counter = counter + 1
  # If we reach the end of the sequence
  # start again
  if (StepCounter>=StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount+StepDir
  if (counter == 100):
      run = False
  # Wait before moving on
  time.sleep(0)






with open('config/HardwareConfig.json') as data_file:
    hardwareData = json.load(data_file)
def getId():
    return hardwareData['StepperMotor']['id']

def update(state):
    try:
        print('ok')
    except:
        return False

    return True
