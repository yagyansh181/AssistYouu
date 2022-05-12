import serial.tools.list_ports
import time

state=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]

ports = list(serial.tools.list_ports.comports())
chk=0
s=None

for p in ports:
    if "Arduino" in p.description:
        print("This is an Arduino!" ," ",p)
        s=p.device
        chk=1
if not chk:
    print("Arduino not found!!!-Connect Arduino")
    exit()

ard = serial.Serial(s,9600,timeout=5)

def command(com):
    c1=com[0]
    c2=com[1]
    if c1== 'u' or c1== 'd':
        ard.write(com.encode('utf-8'))
        temp='s'+c2
        time.sleep(1.0245)
        ard.write(temp.encode('utf-8'))
        read = ard.read().decode('utf-8')
        if ord(c2) > 64:
            tmp = ord(c2) - 55
        else:
            tmp = int(c2)
        state[tmp] = int(read)
        print('Done !')


    elif c1 == 's':
        # ard.write(com.encode('utf-8'))
        # read = ard.read().decode('utf-8')
        if ord(c2) > 64  :
            tmp=ord(c2)-55
        else:
            tmp=int(c2)
        # state[tmp]=int(read)
        # print(int(read))
        print(state[tmp])
    else:
        print("INVALID COMMAND !!!")