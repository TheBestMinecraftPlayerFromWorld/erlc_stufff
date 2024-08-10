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
import startMc,schwVote,rblxErlc,huetest,mcl
#import starterBashes as sb
sb = [print,print,print,print,mcl.start,huetest.switchLights,schwVote.getCmd,rblxErlc.run,startMc.getCmd]
ser = None
ser = serial.Serial("COM4",115200)
while True:
    line = ser.readline().decode("ascii").strip()
    print(line)
    line = int(line)-1
    line = sb[line]
    line()
#ser.close()