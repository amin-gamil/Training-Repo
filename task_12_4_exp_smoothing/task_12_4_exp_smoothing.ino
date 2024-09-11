int motor = 9;
float sf = 0.9;
float target = 255;
float speed = 0;
void setup() {
  pinMode(motor,OUTPUT);
}

void loop() {

  speed = sf * target + (1 - sf) * speed;
  analogWrite(motor, speed);
  delay(50);

}
