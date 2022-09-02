import serial
from flask import Flask
from flask import render_template #要新增資料夾templates
import time
import pymysql


db = pymysql.connect(host="localhost", user="tmpuser", password="hope0406", database="sqlsystem", charset="utf8")
cursor = db.cursor()
ser = serial.Serial("COM12",9600,timeout=0.5)

time.sleep(2)
app = Flask(__name__)
@app.route('/data')
def data():
    ser.open
    if True:
        data1={"0":"0"}
        date1={"0":"0"}
        line = ser.readline()
        if line!=b'' and line != b'Parallax RFID Card Reader\r\n':
            localtime = time.localtime()
            Str = line.decode().split("'")
            d = Str[0].replace("\r","").replace("\n","")
            if(d.split('#')[0]=='Get Card'):
                d = d.split('#')[1]
                print(d)
                data1[1] = d
                date1[1] = time.strftime("%Y%m%d%I%M%S", localtime)
                data = [data1]
                date = [date1]
                sql = "INSERT INTO `test`(`time`, `temperate`) VALUES('{0}','{1}')"
                sql = sql.format(date1[1],
                                 data1[1])
                print(sql)
                try:
                    cursor.execute(sql)  
                    db.commit() 
                    print("新增一筆記錄...")
                except:
                    db.rollback() 
                    print("新增記錄失敗...")
        time.sleep(0.1)
    return render_template("data.html", **locals())
    ser.close()
    db.close()
if __name__ == '__main__':
    app.run()