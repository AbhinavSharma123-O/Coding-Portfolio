// C++ code
//
const byte led1=10;
const byte led2=4;
void setup()
{
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  
}

void loop()
{
  digitalWrite(led1, HIGH);
  digitalWrite(led2,LOW);
  delay(1000);
  digitalWrite(led1, LOW);
  digitalWrite(led2,HIGH);
  delay(1000);
 
  
 
  // Wait for 1000 millisecond(s) 
}