#include <SPI.h>
#include <SD.h>
#include <SoftwareSerial.h>

#define SOFTSERIAL_MainProcessor_RX 6
#define SOFTSERIAL_MainProcessor_TX 7
SoftwareSerial SERIAL_MainProcessor (SOFTSERIAL_MainProcessor_RX, SOFTSERIAL_MainProcessor_TX);
#define SDINFOPIN 5

const int chipSelect = 4;
String logfilename = "log";
bool sderror = true;

void writeToSd(String &data){
  File dataFile = SD.open(logfilename, FILE_WRITE);

  // if the file is available, write to it:
  if (dataFile) {
    digitalWrite(LED_BUILTIN, true);
    digitalWrite(SDINFOPIN, true);
    dataFile.print(data);
    dataFile.close();
    // print to the serial port too:
    Serial.println(data);
  }
  // if the file isn't open, pop up an error:
  else {
    //Serial.println("false");
    digitalWrite(LED_BUILTIN, false);
    digitalWrite(SDINFOPIN, false);
  }
}


void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(SDINFOPIN, OUTPUT);
  digitalWrite(SDINFOPIN, true);
  // Open serial communications and wait for port to open:
  
  
  Serial.begin(9600);
  SERIAL_MainProcessor.begin(9600);

  //SERIAL_MainProcessor.setTimeout(5000);
  //Serial.println(SERIAL_MainProcessor.readStringUntil('\n'));
  

  //Serial.print("Initializing SD card...");

  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    //Serial.println("Card failed, or not present");
    // don't do anything more:
    digitalWrite(LED_BUILTIN, true);
    digitalWrite(SDINFOPIN, false);
    while (true){
      //SERIAL_MainProcessor.println("SD:ERROR#");
      //Serial.println("SD:ERROR");
      delay(500);
    }
  }else{
    //SERIAL_MainProcessor.println("SD:OK#");
  }


  byte i=0;
  String tempname = logfilename;
  while(SD.exists(tempname + ".csv")){
    tempname = logfilename + "_" + i;
    i++;
  }
  logfilename = tempname + ".csv";

  writeToSd("" + String("mcp9808_temperature;"));
  writeToSd("" + String("hp206_pressure;"));
  writeToSd("" + String("hp206_temperature;"));
  writeToSd("" + String("hp206_altitude;"));
  writeToSd("" + String("th02_temperature;"));
  writeToSd("" + String("th02_humidity;"));
  writeToSd("" + String("uv_index;"));
  writeToSd("" + String("tsl2591_light;"));
  writeToSd("" + String("ccs811_eco2;"));
  writeToSd("" + String("ccs811_tvoc;"));
  writeToSd("" + String("sds011_pm25;"));
  writeToSd("" + String("sds011_pm10;"));
  writeToSd("" + String("gps_data_gpgga;"));
  writeToSd("" + String("gps_data_gprmc;\n"));
}

String csvstring;

void loop() {
  //if (SERIAL_MainProcessor.available()){
  //  Serial.print((char) SERIAL_MainProcessor.read());
  //}

  float mcp9808_temperature;
  float hp206_pressure;
  float hp206_temperature;
  float hp206_altitude;
  float th02_temperature;
  float th02_humidity;
  byte uv_index;
  float tsl2591_light;
  float ccs811_eco2;
  float ccs811_tvoc;
  float sds011_pm25;
  float sds011_pm10;
//  String gps_data_gpgga;
//  String gps_data_gprmc;

  SERIAL_MainProcessor.setTimeout(1200);
  String data = SERIAL_MainProcessor.readStringUntil('\n');

  if (data.startsWith("!#")){
    while (!data.startsWith("#!")){
      data = SERIAL_MainProcessor.readStringUntil('\n');
      if (data.startsWith("mcp9808_temperature:")){
        mcp9808_temperature = data.substring(data.indexOf(':')+1).toFloat();
        writeToSd(String(mcp9808_temperature) + ";");
      }
      if (data.startsWith("hp206_pressure:")){
        hp206_pressure = data.substring(data.indexOf(':')+1).toFloat();
        writeToSd(String(hp206_pressure) + ";");
      }
      if (data.startsWith("hp206_temperature:")){
        hp206_temperature = data.substring(data.indexOf(':')+1).toFloat();
        writeToSd(String(hp206_temperature) + ";");
      }
      if (data.startsWith("hp206_altitude:")){
        hp206_altitude = data.substring(data.indexOf(':')+1).toFloat();
        writeToSd(String(hp206_altitude) + ";");
      }
      if (data.startsWith("th02_temperature:")){
        th02_temperature = data.substring(data.indexOf(':')+1).toFloat();
        writeToSd(String(th02_temperature) + ";");
      }
      if (data.startsWith("th02_humidity:")){
        th02_humidity = data.substring(data.indexOf(':')+1).toFloat();
        writeToSd(String(th02_humidity) + ";");
      }
      if (data.startsWith("uv_index:")){
        uv_index = data.substring(data.indexOf(':')+1).toInt();
        writeToSd(String(uv_index) + ";");
      }
      if (data.startsWith("tsl2591_light:")){
        tsl2591_light = data.substring(data.indexOf(':')+1).toFloat();
        writeToSd(String(tsl2591_light) + ";");
      }
      if (data.startsWith("ccs811_eco2:")){
        ccs811_eco2 = data.substring(data.indexOf(':')+1).toFloat();
        writeToSd(String(ccs811_eco2) + ";");
      }
      if (data.startsWith("ccs811_tvoc:")){
        ccs811_tvoc = data.substring(data.indexOf(':')+1).toFloat();
        writeToSd(String(ccs811_tvoc) + ";");
      }

      if (data.startsWith("sds011_pm25:")){
        sds011_pm25 = data.substring(data.indexOf(':')+1).toFloat();
        writeToSd(String(sds011_pm25) + ";");
      }
      if (data.startsWith("sds011_pm10:")){
        sds011_pm10 = data.substring(data.indexOf(':')+1).toFloat();
        writeToSd(String(sds011_pm10) + ";");
      }
      if (data.startsWith("$GPGGA")){
        //gps_data_gpgga = data;
        writeToSd("" + data.substring(0, data.length()-2));
        writeToSd("" + String(";"));
      }
      if (data.startsWith("$GPRMC")){
        //gps_data_gprmc = data;
        writeToSd("" + data.substring(0, data.length()-2));
        writeToSd("" + String(";"));
      }

      //Serial.println(data);
      //Serial.println(csvstring);
      //data = SERIAL_MainProcessor.readStringUntil('\n');
      //csvstring = csvstring + data;
    }
    //Serial.println(csvstring);
    writeToSd("" + String("\n"));
  }
  //Serial.println(data);

}