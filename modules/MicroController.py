import time
import datetime
from modules import StepperMotor

currentState = 0 # blinds always start closed open

def getState():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return {'timestamp': st, 'state': currentState, 'StepperMotor':StepperMotor.getId()}

def updateState(state):
    global currentState
    if(state != 1 and state != 0):
        return False
    if(state == currentState):
        return True
    else:
        currentState = state
        return StepperMotor.update(state)
