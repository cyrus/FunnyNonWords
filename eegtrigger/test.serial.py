import serial
import time
ser = serial.Serial('/dev/cu.usbserial-ALHCTCQ',57600)
print(ser.name)
items = ['1','2','1','2','1','2','1','2','1','2','1','2','1','2','1','2','1','2','1','2']
for item in items:
    ser.write(item)
    time.sleep(0.10)
ser.close()
