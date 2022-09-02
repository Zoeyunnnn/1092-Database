from flask import Flask
app = Flask(__name__)

from flask import request, abort, render_template
from bs4 import BeautifulSoup
import pymysql
import time

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from urllib.parse import parse_qsl

db = pymysql.connect(host="localhost", user="joe", password="a2215939", database="joe", charset="utf8")
cursor = db.cursor()
line_bot_api = LineBotApi('II9hCzAxXspRG1NqZxaalvcEms3i6fcI7guZoqUXP652Riz5bh6Rt+uqnhKHv/yFrFReH0QwnM8RHGDQlt5CljDsg54H+1ASJFQkNzHRgNJFiz/js9uhj47ymtG0IpxUtzdojs+LOZrX6zVDoi1aTwdB04t89/1O/w1cDnyilFU=')#Channel access token (long-lived)
handler = WebhookHandler('4c12914b9024634ca0acefb216da0143')#Channel secret 

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    # get request body as text
    body = request.get_data(as_text=True)
    
    # handle webhook body
    try:
        handler.handle(body ,signature)
    except InvalidSignatureError():
        abort(400)
        
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #鸚鵡模式
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
    print(event.message.text)
    localtime = time.localtime()
    date = time.strftime("%Y%m%d%I%M%S", localtime)
    sql = "INSERT INTO `text`(`message`, `time`) VALUES ('{0}','{1}')"
    sql = sql.format(event.message.text,
                     date)
    print(sql)
    try:
        cursor.execute(sql)   # 執行SQL指令
        db.commit() # 確認交易
        print("新增一筆記錄...")
    except:
        db.rollback() # 回復交易 
        print("新增記錄失敗...")
if __name__ == '__main__':
    app.run()