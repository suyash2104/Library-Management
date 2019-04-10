import serial

data = serial.Serial("/dev/cu.usbmodem14101", 9600)

def s_rfid():
    mydata = data.readline().strip()
    return  (mydata.decode("utf-8"))


def w_rf_data(c):
    data.write(c.encode())
