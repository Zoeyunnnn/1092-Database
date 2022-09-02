int INA = 9; 
int INB = 8;
void setup(){
  pinMode(INA,OUTPUT);
  pinMode(INB,OUTPUT);
}

void loop(){
  digitalWrite(INA,LOW);
  digitalWrite(INB,HIGH);

  delay(1000);
}
