import serial
import time
ser=serial.Serial("COM3",9600,timeout=0.5)
ser.open
time.sleep(3) #間隔3秒
i=1 #好看
while True:
    line = ser.readline()
    if line!=b'':
        print("data"+str(i)+":") #好看+1
        Str = line.decode().split("'") #切割出未整理資料
        data = Str[0].replace("\r","").replace("\n","") #替換多於字符
        for j in data.split(" "): 
            print(j)
        i+=1
    time.sleep(0.1)
ser.close()
