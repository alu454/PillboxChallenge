# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 11:56:16 2020
@author: cibrian
"""

import serial
import pandas as pd

arduino=serial.Serial('COM3',9600)
df = pd.DataFrame(columns = ["AcX","AcY","AcZ", "Tmp","GyX","GyY","GyZ"])
df.to_csv('test.csv', index=False)

while True:
    while(arduino.inWaiting()==0):
        pass
 
    arduinostring=arduino.readline()
    arduinostring=str(arduinostring,encoding="utf-8")
    print (arduinostring)
    dataArray=arduinostring.split(' | ')
    index = len(df.index)
    print (dataArray)


    df.loc [index] = [
        dataArray[0].split("=")[1],
        dataArray[1].split("=")[1],
        dataArray[2].split("=")[1],
        dataArray[3].split("=")[1],
        dataArray[4].split("=")[1],
        dataArray[5].split("=")[1],
        dataArray[6].split("=")[1].replace("\r\n", "")]

    print (df)
    df.loc[index:].to_csv('test.csv', index= False, mode='a', header=False)
