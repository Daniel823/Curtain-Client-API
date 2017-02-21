import time
import datetime

def getState():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return {'timestamp': st, 'state': 0}

def updateState(action):
    
    return True
