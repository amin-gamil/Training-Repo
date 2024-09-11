  double input,output,error,past;
  double kp = 5;
  double ki = 0;
  double kd = 0;
  double speed = 0;
  long int t1,t2;

void setup() {
  // put your setup code here, to run once:

  t1 = millis();

}

void loop() {
  // put your main code here, to run repeatedly:
  speed = pid();
  delay(1000);
}

float pid(){
  input = input; // read sensor data
  error = output - input;
  t2 = millis();
  output = kp * error + ki * error * (t2 - t1) + kd * (error - past)/(t2 - t1);
  t1 = t2;
  past = error;
  return output;
}