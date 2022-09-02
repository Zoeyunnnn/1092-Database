#define Do  523
#define Re  587
#define Mi  659
#define Fa  698
#define So  784
#define La  880
#define Si  988
int melody[24] = {So, Mi, Mi, Fa, Re, Re, Do, Re, Mi, Fa, So, So, So, So, Mi, Mi, Fa, Re, Re, Do, Mi, So, So, Mi};
const int buzzer = 8;
void setup() {
  pinMode(buzzer,OUTPUT);
}

void loop() {
  for (int i = 0;i < 24; i++) {
    tone(buzzer, melody[i]);
    delay(500);  
  }
  noTone(buzzer);//不發出聲音
  delay(2000);
}
