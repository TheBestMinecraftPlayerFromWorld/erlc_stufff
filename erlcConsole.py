"""import startMc,time

userNames = ["Best___Player","Mister_Dirt","John"]
server   = "schwimmnudel.net:2006"

for userName in userNames:
    startMc.startMc(userName,server)
    time.sleep(10)
"""
import serial
import serial.tools
import serial.tools.list_ports
import keyboard
import time
import erlcAutoChat as eac
#import starterBashes as sb
ser = None
ser = serial.Serial("COM4",115200)
states = [0,0,0,511,511]
lastStates = [0,0,0,511,511]
lightState = 0
sirenState = 0

def lightsOn():
    global lightState
    if lightState == 1:
        return
    lightState = 1
    print("Lights on!")
    keyboard.press_and_release("x")
    time.sleep(0.5)
    keyboard.press_and_release("x")
    time.sleep(0.5)
    keyboard.press_and_release("x")
def lightsOff():
    global lightState
    if lightState == 0:
        return
    lightState = 0
    print("Lights off!")
    keyboard.press_and_release("x")
tv = 0
while True:
    line = ser.readline().decode("ascii").strip()
    states = line.split(";")
    try:
        states.remove("")
    except:
        pass
    if len(states)<5:
        continue
    states = [int(state) for state in states]
    states[0] = 1-states[0]
    states[3]-=512
    states[4]-=512
    if lastStates[0] != states[0]:
        if states[0] == 1:
            lightsOn()
        else:
            lightsOff()
    if lastStates[1] != states[1]:
        if states[1] == 1:
            eac.start_recording()
        else:
            eac.stop_recording()
    if lastStates[2] != states[2]:
        if states[2] == 1:
            if states[0]==0:
                lightsOn()
            sirenState = 1
            print("Siren on!")
            keyboard.press_and_release("c")
        else:
            sirenState = 0
            print("Siren off!")
            lightsOff()
            if states[0] == 1:
                lightsOn()

    
    """if abs(states[3])>=tv:
        if states[3]>0:
            keyboard.press_and_release("d")
            time.sleep(0.1)
        else:
            keyboard.press_and_release("a")
            time.sleep(0.1)

    if abs(states[4])>=tv:
        if states[4]>0:
            keyboard.press_and_release("w")
            time.sleep(0.1)
        else:
            keyboard.press_and_release("s")
            time.sleep(0.1)
    
    tv = (tv+1)%512"""
    lastStates = states
#ser.close()