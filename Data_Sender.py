# Python code transmits a byte to Arduino /Microcontroller
import serial
import time
SerialObj = serial.Serial('COM4') # COMxx  format on Windows
                  # ttyUSBx format on Linux
SerialObj.baudrate = 9600  # set Baud rate to 9600
SerialObj.bytesize = 32   # Number of data bits = 8
SerialObj.parity  ='N'   # No parity
SerialObj.stopbits = 1   # Number of Stop bits = 1
time.sleep(3)


def write_read(x): 
    SerialObj.write(bytes(x, 'utf-8')) 
    time.sleep(0.05)

