import serial
import time
from flask import Flask
from flask import render_template 

ser=serial.Serial("COM12",9600,timeout=0.5)
ser.open
time.sleep(3) #間隔3秒
app = Flask(__name__)
@app.route('/data')
def data():
    i=1
    dic={}
    while True:
        line = ser.readline()
        if line!=b'':
            c=1
            print("data"+str(i)+":")
            Str = line.decode().split("'")
            data = Str[0].replace("\r","").replace("\n","")
            for j in data.split(" "): 
                print(j)
                dic[c]=j
                c+=1
            i+=1
        time.sleep(0.1)
    return render_template("data.html", **locals())
ser.close()

if __name__ == '__main__':
    app.run()