import serial

data = serial.Serial("/dev/cu.usbmodem14201", 9600)

def rfid_data():
    mydata = data.readline().strip()
    return  (mydata.decode("utf-8"))

if __name__ == "__main__":
    while True:
        print(rfid_data())
