long randNumber;
String str;
char total[20];
char sum[20];
int i=0;

byte * readSensors() {
   static byte s[20];
   
   for (byte i=0; i<20; i++) {
     s[i] = random(300);
   }
   return s;
}
void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  byte *pt = readSensors();
  for (byte i=0; i<20; i++) {
    Serial.print(*(pt+i));
    Serial.print(" ");  
  }
  Serial.println("");
  
  delay(5000);
}
