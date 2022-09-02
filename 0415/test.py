import serial
import time
import pymysql
import requests
from bs4 import BeautifulSoup
import re

db = pymysql.connect(host="localhost", user="tmpuser", password="hope0406", database="sqlsystem", charset="utf8")
cursor = db.cursor()
ser = serial.Serial("COM12",9600,timeout=0.5)

time.sleep(2)
ser.open
while True:
    line = ser.readline()
    if line!=b'' and line != b'Safe#\r\n':
        localtime = time.localtime()
        Str = line.decode().split("'")
        d = Str[0].replace("\r","").replace("\n","")
        if(d.split('#')[0]=='Error'):
            d = d.split('#')[1]
            print(d)
            data = d
            date = time.strftime("%Y%m%d%I%M%S", localtime)
            
            url = "time:"+date+" 溫溼度:"+data
            data1 = "http://api.thingspeak.com/update?api_key=PZQR1HX7QFJ5P4G8&field1="+url
            url = requests.get(data1, headers={'Connection':'close'})
            url.encoding = 'big5'
            soup = BeautifulSoup(url.text,"html.parser")
            
            sql = "INSERT INTO `test2`(`temperate`, `time`) VALUES('{0}','{1}')"
            sql = sql.format(data,
                             date)
            print(sql)
            try:
                cursor.execute(sql)  
                db.commit() 
                print("新增一筆記錄...")
            except:
                db.rollback() 
                print("新增記錄失敗...")
    time.sleep(15)
ser.close()
db.close()