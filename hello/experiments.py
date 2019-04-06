
import serial

data = serial.Serial("/dev/cu.usbmodem14201", 9600)

while True:
    mydata = data.readline().strip()
    print(mydata.decode('utf-8'))