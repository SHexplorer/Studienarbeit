#include <Arduino.h>
#include <SoftwareSerial.h>

/*
#ifdef __arm__
// should use uinstd.h to define sbrk but Due causes a conflict
extern "C" char* sbrk(int incr);
#else  // __ARM__
extern char *__brkval;
#endif  // __arm__

int freeMemory() {
  char top;
#ifdef __arm__
  return &top - reinterpret_cast<char*>(sbrk(0));
#elif defined(CORE_TEENSY) || (ARDUINO > 103 && ARDUINO != 151)
  return &top - __brkval;
#else  // __arm__
  return __brkval ? &top - __brkval : &top - __malloc_heap_start;
#endif  // __arm__
}
*/

#define SOFTSERIAL_SDS011_RX 9
#define SOFTSERIAL_SDS011_TX 10
SoftwareSerial SERIAL_SDS011(SOFTSERIAL_SDS011_RX, SOFTSERIAL_SDS011_TX);
#define SOFTSERIAL_CoProcessor_RX 11
#define SOFTSERIAL_CoProcessor_TX 6
SoftwareSerial SERIAL_CoProcessor(SOFTSERIAL_CoProcessor_RX, SOFTSERIAL_CoProcessor_TX);
#define SDINFOPIN 5


#include "sensors.h"
#include "lora.h"

bool sderror;

void sendAndLog(String &data){
  send_RFM95(data);
  SERIAL_CoProcessor.println(data);
  //Serial.println(data);
}

void setup() {
  pinMode(SDINFOPIN, INPUT_PULLUP);
  SERIAL_CoProcessor.begin(9600);
  //Serial.begin(9600);
  //while (!Serial)
  
  delay(500);
  //Serial.println("Starting");

  init_RFM95();
  init_CCS811();
  init_MCP9808();
  init_TSL2591();
  init_HP206();
  init_TH02();
  init_SDS011();
  init_gps();

  delay(5000);
}

void loop() {
  /*
  Serial.println("");
  Serial.println("CCS811:");
  Serial.println(get_CCS811_eCO2());
  Serial.println(get_CCS811_TVOC());

  Serial.println("");
  Serial.println("MCP9808:");
  Serial.println(get_MCP9808_temperature());

  Serial.println("");
  Serial.println("TSL2591:");
  Serial.println(get_TSL2591_light());


  Serial.println("");
  Serial.println("HP206:");
  Serial.println(get_HP206_pressure());
  Serial.println(get_HP206_altitude());
  Serial.println(get_HP206_temperature());

  //Serial.println("");
  //Serial.println("SDS011:");
  //Serial.println(get_SDS011_PM25());
  //Serial.println(get_SDS011_PM10());

  Serial.println("");
  Serial.println("UV:");
  Serial.println(get_UV_Index());

  Serial.println("");
  Serial.println("GPS:");
  Serial.println(get_gps_data());


  //TIMESTAMP;MCP9808_TEMP;TH02_HUM;HP206_PRESSURE;HP206_TEMP;HP206_ALT;UV_INDEX;TSL2591_LIGHT;CCS811_ECO2;CCS811_TVOC;SDS011_PM25;SDS011_PM10;GPS_LON;GPS_LAT;GPS_ALT_GPS_NUMSAT;CHECKSUM;\n
  
  
  datastring = "TIMESTAMP";
  strcat(datastring, dtostrf(get_MCP9808_temperature(), , , );
  Serial.println(datastring);
  datastring = datastring + String(get_MCP9808_temperature()) + ";";
  Serial.println(datastring);
  datastring = datastring + String("TH02_HUM") + ";";
  Serial.println(datastring);
  datastring = datastring + String(get_HP206_pressure()) + ";";
  Serial.println(datastring);
  datastring = datastring + String(get_HP206_temperature()) + ";";
  Serial.println(datastring);
  //datastring = datastring + String(get_HP206_altitude()) + ";";
  //Serial.println(datastring);
  //datastring = datastring + String(get_UV_Index()) + ";";
  //Serial.println(datastring);
  //datastring = datastring + String(get_TSL2591_light()) + ";";
  Serial.println(datastring);
  datastring = datastring + String(get_CCS811_eCO2()) + ";";
  Serial.println(datastring);
  datastring = datastring + String(get_CCS811_TVOC()) + ";";
  Serial.println(datastring);
  datastring = datastring + String(get_SDS011_PM25()) + ";";
  Serial.println(datastring);
  datastring = datastring + String(get_SDS011_PM10()) + ";";
  datastring = datastring + "\n";
  */
 /*
  float mcp9808_temperature = get_MCP9808_temperature();
  float hp206_pressure = get_HP206_pressure();
  float hp206_temperature = get_HP206_temperature();
  float hp206_altitude = get_HP206_altitude();
  float th02_temperature = get_TH02_temperature();
  float th02_humidity = get_TH02_humidity();
  int uv_index = get_UV_Index();
  float tsl2591_light = get_TSL2591_light();
  float ccs811_eco2 = get_CCS811_eCO2();
  float ccs811_tvoc = get_CCS811_TVOC();
  //float sds011_pm25 = get_SDS011_PM25();
  //float sds011_pm10 = get_SDS011_PM10();
  String gps_data = get_gps_data();

  datastring = "mcp9808_temperature:" + String(mcp9808_temperature) + ";";
  send_RFM95(datastring);
  datastring = "hp206_pressure:" + String(hp206_pressure) + ";";
  send_RFM95(datastring);
  datastring = "hp206_temperature:" + String(hp206_temperature) + ";";
  send_RFM95(datastring);
  datastring = "hp206_altitude:" + String(hp206_altitude) + ";";
  send_RFM95(datastring);
  datastring = "th02_temperature:" + String(th02_temperature) + ";";
  send_RFM95(datastring);
  datastring = "th02_humidity:" + String(th02_humidity) + ";";
  send_RFM95(datastring);
  datastring = "uv_index:" + String(uv_index) + ";";
  send_RFM95(datastring);
  datastring = "tsl2591_light:" + String(tsl2591_light) + ";";
  send_RFM95(datastring);
  datastring = "ccs811_eco2:" + String(ccs811_eco2) + ";";
  send_RFM95(datastring);
  datastring = "ccs811_tvoc:" + String(ccs811_tvoc) + ";";
  send_RFM95(datastring);
  //datastring = "sds011_pm25:" + String(sds011_pm25) + ";";
  //send_RFM95(datastring);
  //datastring = "sds011_pm10:" + String(sds011_pm10) + ";";
  //send_RFM95(datastring);
  datastring = "gps_data:" + String(gps_data) + ";";
  send_RFM95(datastring);
*/

  //Serial.println(get_TSL2591_light());

  String startend = "!#";
  sendAndLog(startend);
  sendAndLog("mcp9808_temperature:" + String(get_MCP9808_temperature()));
  sendAndLog("hp206_pressure:" + String(get_HP206_pressure()));
  sendAndLog("hp206_temperature:" + String(get_HP206_temperature()));
  sendAndLog("hp206_altitude:" + String(get_HP206_altitude()));
  sendAndLog("th02_temperature:" + String(get_TH02_temperature()));
  sendAndLog("th02_humidity:" + String(get_TH02_humidity()));
  sendAndLog("uv_index:" + String(get_UV_Index()));
  sendAndLog("tsl2591_light:" + String(get_TSL2591_light()));
  sendAndLog("ccs811_eco2:" + String(get_CCS811_eCO2()));
  sendAndLog("ccs811_tvoc:" + String(get_CCS811_TVOC()));
  sendAndLog("sds011_pm25:" + String(get_SDS011_PM25()));
  sendAndLog("sds011_pm10:" + String(get_SDS011_PM10()));
  sendAndLog("" + String(get_gps_GPGGA()));
  sendAndLog("" + String(get_gps_GPRMC()));
  sderror = digitalRead(SDINFOPIN);
  if (sderror)
    send_RFM95(String("SD:OK") + "");
  else
    send_RFM95(String("SD:ERROR") + "");
  startend = "#!";
  sendAndLog(startend);


}