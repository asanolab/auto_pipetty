#include <Servo.h>
# define PWMPin 9
Servo myservo;
int command=0;
void setup()
{
	myservo.attach(PWMPin,700,2000);//top is 0, bottom is 180 (origin: 1000,2000)
  Serial.begin(9600);
  myservo.write(0);
}
void loop()
{
  while (Serial.available()>0)
  {
    command=Serial.read();
    Serial.print(command);
    delay(10);
  }
  if (command==1)
    {
      myservo.write(120);
      delay(500);
      myservo.write(0);
      command=0;
    }
  else
    myservo.write(0);
  delay(10);
}
