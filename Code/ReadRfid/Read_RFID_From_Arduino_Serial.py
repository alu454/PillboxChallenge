def rfid():
    import serial
    ser = serial.Serial()
    ser.baudrate = 9600
    try:
        ser.port = '/dev/ttyACM0'
    except:
        ser.port = '/dev/ttyACM1'
    
    
    ser.open()
    RFID_Data=ser.readline() 
    if RFID_Data:
        RFID_Data = RFID_Data.decode()  #Decode arduino Serial
        RFID_Data = RFID_Data.strip()   #Strip Arduino Data to remove string
        RFID_Data=int(RFID_Data);       #Convert the Data to Int
        return(RFID_Data)
    
            

while(True):
    data = rfid() 
    print(data)