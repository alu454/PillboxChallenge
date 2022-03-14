import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
LED = board.digital[11]
PIR=board.digital[5]
PIR.mode=pyfirmata.INPUT
print("start")

while True:
    if PIR.read() == True:
        LED.write(1)
    else:
        LED.write(0)
