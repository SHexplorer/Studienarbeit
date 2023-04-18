void setup() 
{
  Serial.begin(9600); // Baudrate des seriellen Monitors
}

void loop() 
{
  int SensorWert;
  SensorWert = analogRead(0); // Sensorwert wird an der Schnittstelle A0 ausgelesen...   
  Serial.println(SensorWert);  // ...und anschließend zur Kontrolle im seriellen Monitor ausgegeben.

  if (SensorWert < 10 )      // Wenn der Sensorwert kleiner als 10 ist...
  {
    Serial.println("Index: 0 ");   // ... soll diese Meldung...
    Serial.println("Kein Schutz erforderlich.");  // ... im seriellen Monitor erscheinen.
  }
  
  if (SensorWert < 46 & SensorWert > 10 )  // Wenn der Sensorwert kleiner als 46 und größer als 10 ist...
  {
    Serial.println("Index : 1");    // ...soll diese Meldung...
    Serial.println("Kein Schutz erforderlich.");  // ... im seriellen Monitor erscheinen.
  }
  
  if (SensorWert < 65 & SensorWert > 46 )
  {
    Serial.println("Index : 2");
    Serial.println("Kein Schutz erforderlich.");
  }
  
  if (SensorWert < 83 & SensorWert > 65 )
  {
    Serial.println("Index : 3");
    Serial.println("Schutz erforderlich : z.B. Hut, Sonnencreme");
  }
  
  if (SensorWert < 103 & SensorWert > 83 )
  {
    Serial.println("Index : 4");
    Serial.println("Schutz erforderlich : z.B. Hut, Sonnencreme");
  }
  
  if (SensorWert < 124 & SensorWert > 103 )
  {
    Serial.println("Index : 5");
    Serial.println("Schutz erforderlich : z.B. Hut, Sonnencreme");
  }
  if (SensorWert < 142 & SensorWert > 124 )
  {
    Serial.println("Index : 6");
    Serial.println("Schutz erforderlich : z.B. Hut, Sonnencreme. Schatten aufsuchen.");
  }
  
  if (SensorWert < 162 & SensorWert > 142 )
  {
    Serial.println("Index : 7");
    Serial.println("Schutz erforderlich : z.B. Hut, Sonnencreme. Schatten aufsuchen.");
  }
  
  if (SensorWert < 180 & SensorWert > 162 )
  {
    Serial.println("Index : 8");
    Serial.println("Aufenthalt im Freien möglichst vermeiden. Schutz erforderlich.");
  }
  
  if (SensorWert < 200 & SensorWert > 180 )
  {
    Serial.println("Index : 9");
    Serial.println("Aufenthalt im Freien möglichst vermeiden. Schutz erforderlich.");
  }
  
  if (SensorWert < 221 & SensorWert > 200 ) 
  {
    Serial.println("Index : 10");
    Serial.println("Aufenthalt im Freien möglichst vermeiden. Schutz erforderlich.");
  }

  if (SensorWert > 221 )
  {
    Serial.println("Index : 11");
    Serial.println("Aufenthalt im Freien vermeiden. Schutz DRINGEND erforderlich.");
  }



  
  delay(1000);    /// Delay von einer Sekunde  
}
