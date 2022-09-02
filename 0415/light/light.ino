#include "DHT.h"
#define DHTPIN 7
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
void setup() {
  Serial.begin(9600);
  pinMode(3,OUTPUT);
  dht.begin();
}
//
void loop() {  
  float h = dht.readHumidity();   //取得濕度
  float t = dht.readTemperature();
  Serial.print(h);
  //int sensorValue = analogRead(A0);
  //Serial.println(sensorValue);
//  if(sensorValue > 70){
//    Serial.print("Error#");
//    Serial.print(h);
//    Serial.print("\t");
//    Serial.print(t);
//    Serial.println("*C\t");
//  }else{
//    Serial.println("Safe#");
//  }
  delay(500);
}
