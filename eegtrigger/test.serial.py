#test serial port access
import serial
import time


ser = serial.Serial('/dev/cu.usbserial-ALHCTCQ',57600)
print("Connected to: " + ser.name)
# Each number needs to be in hex
item1 = bytearray.fromhex(u'01')
item2 = bytearray.fromhex(u'ff')
items = [item1,item2]
for item in items:
    ser.write(item)
    time.sleep(0.2)
ser.close()
print("Finished!")
