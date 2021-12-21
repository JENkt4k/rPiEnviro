# this is read_serial.py
import serial 
from time import sleep
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

while True:
  if ser.inWaiting() > 0: # if ser.in_waiting > 0:
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    #sleep(1)