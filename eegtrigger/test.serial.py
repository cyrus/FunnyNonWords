#test serial port access
import serial
import time
ser = serial.Serial('/dev/cu.usbserial-ALHCTCQ',57600)
print(ser.name)
#items = [bytearray([1, 1, 1]),bytearray([1,1, 2]),bytearray([1,1, 3]),bytearray([1,1, 4])]
#items = [bytearray(['\xff']), bytearray(['\x22'])
#items = [bytearray([1]),bytearray([1]),bytearray([1]),bytearray([4])]
#items = [b'x\03','2','1','2','1','2','1','2','1','2','1','2','1','2','1','2','1','2','1','2']
item1 = bytearray.fromhex(u'01')
item2 = bytearray.fromhex(u'ff')
items = [item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2,item1,item2]
for item in items:
    ser.write(item)
    time.sleep(0.01)
ser.close()
