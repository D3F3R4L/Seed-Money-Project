import time
import serial
import os
from datetime import datetime
import RainfallTest

#Initializing CSV file.
ser=serial.Serial("/dev/ttyAMA0",9600,timeout=10)
file = open ("/home/pi/data.csv","a")
if os.stat ("/home/pi/data.csv").st_size==0:
    file.write ("Data,Insolação,TempMax,TempMin,TempMean,Umidade Relativa Media,Precipitação\n")
i=0

#Request and collect data function 
def retrieveData (DataType):
    ser.flushInput()
    ser.flushOutput()
    ser.write(DataType.encode())
    while True:
        try:
            data=ser.readline().decode('utf-8')[:-2]
            return data
        except:
            pass
    time.sleep(0.1)

while True:
    # Request data
    print('Requesting Data...')
    now= datetime.now()
    data1 = retrieveData('1')
    print(data1)
    time.sleep(0.1)
    data2 = retrieveData('2')
    print(data2)
    time.sleep(0.1)
    data3 = retrieveData('3')
    print(data3)
    time.sleep(0.1)
    data4 = retrieveData('4')
    print(data4)
    time.sleep(0.1)
    data5 = retrieveData('5')
    print(data5)
    time.sleep(0.1)
    data6 = retrieveData('6')
    print(data6)
    print('Data Received')
    time.sleep(0.1)
    file.write(str(now)+","+str(data1)+","+str(data2)+","+str(data3)+","+str(data4)+","+str(data5)+","+str(data6)+"\n")
    file.flush()
    time.sleep(1.2)
    i+=1
        # 'if' with Defined Value to use in the neural network
    if i==15:
        print("Calling Machine Learning...")
        i==0
        predict,real=RainfallTest.NeuralNetwork()
        file = open ("/home/pi/result.csv","a")
        if os.stat ("/home/pi/result.csv").st_size==0:
            file.write ("Predicted_Result, Real_result\n")
        j=0
        while j<len(predict):
            file.write(str(predict[j][0])+","+str(real[j])+"\n")
            j+=1
        quit() #just for test