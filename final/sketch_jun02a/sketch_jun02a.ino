#include <SoftwareSerial.h>
#include <Wire.h>
#include "DHT.h"
#define DHTPIN 7
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

 
#include <Wire.h>
  
int LED = 2;//接5V、GND、pin2
SoftwareSerial BT(10,11);//藍芽接5V、GND、(TXD)pin10、(RXE)11
  
void setup() {
  BT.begin(9600);
  pinMode(LED, OUTPUT);    
  Serial.begin(9600);
  dht.begin();
}
  
void loop() {
  byte cmd[20];
  int strsize;
  while(true){
    if ((strsize=(BT.available()))>0){
      for (int i=0; i<strsize; i++){
        cmd[i]=char(BT.read());
      }
      Serial.println(cmd[0]);
    }
    if (cmd[0]=='O') {//燈開
      digitalWrite(LED, HIGH);
    } else if (cmd[0]=='X') {//燈關
      digitalWrite(LED, LOW);
    } 
      }else if (cmd[0]=='Y') {//門開
        
      }else if (cmd[0]=='N') {//門關
        
      }else if (cmd[0]=='A') {//風扇開
        
      }else if (cmd[0]=='B') {//風扇關
        
      }else if (cmd[0]=='C') {//溫溼度
      float h = dht.readHumidity();
      float t = dht.readTemperature();
      Serial.println(h);
      Serial.println(t);
      char hum_buf[10], tem_buf[10];
      if (!isnan(h) && !isnan(t)) {
        dtostrf(h, 3, 2, hum_buf);
        dtostrf(t, 3, 2, tem_buf);
        for(int i=0; i<5; i++) {
          BT.write(hum_buf[i]);
        }
        for(int i=0; i<5; i++) {
          BT.write(tem_buf[i]);
        }
      cmd[0]='d';
    }
  } 
   
}
