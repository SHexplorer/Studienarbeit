void setup() 
{
  Serial.begin(9600); // Baudrate des seriellen Monitors
}

void loop() 
{
  int SensorWert;
  SensorWert = analogRead(0); // Sensorwert wird an der Schnittstelle A0 ausgelesen...   
  Serial.println(SensorWert);  // ...und anschließend zur Kontrolle im seriellen Monitor ausgegeben.

 delay(1000);    /// Delay von einer Sekunde  
}
