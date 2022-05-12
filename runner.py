import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
chk=0
for p in ports:
    if "Arduino" in p.description:
        print(p.device)
        print("This is an Arduino!" ," ",p)
        chk=1
if not chk:
    print("Arduino not found")