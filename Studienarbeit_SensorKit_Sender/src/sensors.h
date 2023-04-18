//#include "Adafruit_CCS811.h"
//#include "ccs811.h"
#include "DFRobot_CCS811.h"
//#include "Adafruit_MCP9808.h"
#include <mcp9808.h>
#include "Adafruit_TSL2591.h"
#include <TSL2591TwoWire.h>

#include <HP206C.h>
#include <TH02_dev.h>

#include "SdsDustSensor.h"

//#include <MicroNMEA.h>

//Adafruit_CCS811 ccs;
//CCS811 ccs811 = CCS811();
DFRobot_CCS811 CCS811;


//Adafruit_MCP9808 tempsensor = Adafruit_MCP9808();

Adafruit_TSL2591 tsl = Adafruit_TSL2591(2591); // pass in a number for the sensor identifier (for your use later)
//TSL2591TwoWire tsl2591(&Wire);   //using SDA  / SCL
SdsDustSensor sds(SERIAL_SDS011); // passing HardwareSerial& as parameter
HP206C hp;

//char nmeaBuffer[100];
//MicroNMEA nmea(nmeaBuffer, sizeof(nmeaBuffer));


bool init_SDS011(){
  sds.begin();
  return true;
}

float get_SDS011_PM25(){
  PmResult pm = sds.queryPm();
  if (pm.isOk()) 
    return pm.pm25;
  else
    return -1;
}

float get_SDS011_PM10(){
  PmResult pm = sds.queryPm();
  if (pm.isOk()) 
    return pm.pm10;
  else
    return -1;
}


bool init_MCP9808(){
  const int8_t error = Mcp9808.begin(); // Rev2
  if (error) {
    return false;
  }
  Mcp9808.setResolution(res_00625);
  return true;
}

float get_MCP9808_temperature(){
  return Mcp9808.readTempC();
}

bool init_HP206(){
  hp.getAddr_HP206C(HP206C_DEFAULT_ADDRESS);          // 0x76
  hp.setOSR(OSR_4096);            // OSR=4096
  hp.begin();
  byte error;
  int8_t address;

  address = hp.hp_i2cAddress;
  // The i2c_scanner uses the return value of
  // the Write.endTransmisstion to see if
  // a device did acknowledge to the address.
  Wire.beginTransmission(address);
  error = Wire.endTransmission();
  if (error == 0)
    return true;
  else
    return false;
}

float get_HP206_temperature(){
  hp.Measure_Sensor();
  return hp.hp_sensorData.T;
}

float get_HP206_pressure(){
  hp.Measure_Sensor();
  return hp.hp_sensorData.P;
}

float get_HP206_altitude(){
  hp.Measure_Sensor();
  return hp.hp_sensorData.A;
}

bool init_TH02(){
  TH02.begin();
  if(TH02.isAvailable()){
    return true;
  }
  //Serial.println("TH02 init failed");
  return false;
}

float get_TH02_temperature(){
  return TH02.ReadTemperature();
}

float get_TH02_humidity(){
  return TH02.ReadHumidity();
}

/*
bool init_TSL2591(){
  if (!tsl2591.begin())
  {
    //Serial.println("begin() failed. check the connection to your TSL2591.");
  }
  tsl2591.resetToDefaults();  

  //set channel
  tsl2591.setChannel(TSL2591MI::TSL2591_CHANNEL_0);

  //set gain
  tsl2591.setGain(TSL2591MI::TSL2591_GAIN_MED);

  //set integration time
  tsl2591.setIntegrationTime(TSL2591MI::TSL2591_INTEGRATION_TIME_100ms);

  return true;
}

float get_TSL2591_light(){
  if (!tsl2591.measure())
  {
    //Serial.println("could not start measurement. ");
    return -1;
  }

  //wait for both measurement to finish
  do
  {
    delay(100);
  } while (!tsl2591.hasValue());

  return tsl2591.getBrightness(); 
}
*/

bool init_TSL2591(){
  if (!tsl.begin())
  {
    //Serial.println("begin() failed. check the connection to your TSL2591.");
  }
  //set channel
  tsl.setGain(TSL2591_GAIN_MED);      // 25x gain

  //set gain
  tsl.setTiming(TSL2591_INTEGRATIONTIME_100MS);

  //set integration time

  return true;
}

uint16_t get_TSL2591_light(){
  return tsl.getLuminosity(TSL2591_VISIBLE);
}

bool init_CCS811(){
  if(CCS811.begin() != 0){
    return false;
  }
  return true;
}

uint16_t get_CCS811_eCO2(){
  return CCS811.getCO2PPM();
}

uint16_t get_CCS811_TVOC(){
  return CCS811.getTVOCPPB();
}


byte get_UV_Index(){
  byte SensorWert = analogRead(0);
  if (SensorWert < 10 )      // Wenn der Sensorwert kleiner als 10 ist...
  {
    return 0;
  }
  
  if (SensorWert < 46 & SensorWert > 10 )  // Wenn der Sensorwert kleiner als 46 und größer als 10 ist...
  {
    return 1;
  }
  
  if (SensorWert < 65 & SensorWert > 46 )
  {
    return 2;
  }
  
  if (SensorWert < 83 & SensorWert > 65 )
  {
    return 3;
  }
  
  if (SensorWert < 103 & SensorWert > 83 )
  {
    return 4;
  }
  
  if (SensorWert < 124 & SensorWert > 103 )
  {
    return 5;
  }
  if (SensorWert < 142 & SensorWert > 124 )
  {
    return 6;
  }
  
  if (SensorWert < 162 & SensorWert > 142 )
  {
    return 7;
  }
  
  if (SensorWert < 180 & SensorWert > 162 )
  {
    return 8;
  }
  
  if (SensorWert < 200 & SensorWert > 180 )
  {
    return 9;
  }
  
  if (SensorWert < 221 & SensorWert > 200 ) 
  {
    return 10;
  }

  if (SensorWert > 221 )
  {
    return 11;
  }
}

bool init_gps(){
  Serial1.begin(4800);
  return true;
}

bool nmea_checksum(String &data){
  int i;
  unsigned char XOR;
  byte ilen;

  ilen = data.indexOf('*');
  for (XOR=0,i=1;i<ilen;i++){
    XOR ^= data[i];
  }
  if (data.substring(data.indexOf('*')+1).compareTo(String(XOR)))
    return true;
  else
    return false;
}

String get_gps_GPGGA(){
  String gpsStream = "";
  Serial1.setTimeout(100);
  for (byte i = 0; i<20; i++){
    if (Serial1.available()) {
      gpsStream=Serial1.readStringUntil(10);   //NMEA data ends with 'return' character, which is ascii(13)
      if (gpsStream.startsWith("$GPGGA") && nmea_checksum(gpsStream)){
        gpsStream.replace("\x00", "");
        gpsStream.replace("\r", "");
        gpsStream.replace("\n", "");
        return gpsStream;
      }
    }
    delay(50);
  }
  return "-";
}

String get_gps_GPRMC(){
  String gpsStream = "";
  Serial1.setTimeout(100);
  for (byte i = 0; i<20; i++){
    if (Serial1.available()) {
      gpsStream=Serial1.readStringUntil(10);   //NMEA data ends with 'return' character, which is ascii(13)
      if (gpsStream.startsWith("$GPRMC") && nmea_checksum(gpsStream)){
        gpsStream.replace("\x00", "");
        gpsStream.replace("\r", "");
        gpsStream.replace("\n", "");
        return gpsStream;
      }
    }
    delay(50);
  }
  return "-";
}
