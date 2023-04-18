import sys
import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QFile, QIODevice, QCoreApplication
from PySide6.QtGui import QIcon
from PySide6 import QtSerialPort
from PySide6 import QtCore

import pynmeagps
import datetime

#import utils

class MainUI(QWidget):
    """
    Method to load the UI. 
    """
    def load_ui(self):
        ui_file_name = "main.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)
        loader = QUiLoader()
        loader.load(ui_file, self)
        ui_file.close()
    
    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.load_ui()
        self.setWindowTitle("Sensorkit Main UI")
        self.image = None

        self.pte_serial_console: QPlainTextEdit = self.findChild(QPlainTextEdit, "pte_serial_console")
        self.cb_serial_ports: QComboBox = self.findChild(QComboBox, "cb_serial_ports")


        self.l_mcp9808_value: QLabel = self.findChild(QLabel, "l_mcp9808_value")
        self.l_hp206_pressure_value: QLabel = self.findChild(QLabel, "l_hp206_pressure_value")
        self.l_hp206_temperature_value: QLabel = self.findChild(QLabel, "l_hp206_temperature_value")
        self.l_hp206_altitude_value: QLabel = self.findChild(QLabel, "l_hp206_altitude_value")
        self.l_th02_humidity_value: QLabel = self.findChild(QLabel, "l_th02_humidity_value")
        self.l_th02_temperature_value: QLabel = self.findChild(QLabel, "l_th02_temperature_value")
        self.l_uv_index_value: QLabel = self.findChild(QLabel, "l_uv_index_value")
        self.l_tsl2591_light_value: QLabel = self.findChild(QLabel, "l_tsl2591_light_value")
        self.l_sds011_pm25_value: QLabel = self.findChild(QLabel, "l_sds011_pm25_value")
        self.l_sds011_pm10_value: QLabel = self.findChild(QLabel, "l_sds011_pm10_value")
        self.l_ccs811_eco2_value: QLabel = self.findChild(QLabel, "l_ccs811_eco2_value")
        self.l_ccs811_tvoc_value: QLabel = self.findChild(QLabel, "l_ccs811_tvoc_value")
        self.l_sd_value: QLabel = self.findChild(QLabel, "l_sd_value")

        self.l_gps_laengengrad_value: QLabel = self.findChild(QLabel, "l_gps_laengengrad_value")
        self.l_gps_breitengrad_value: QLabel = self.findChild(QLabel, "l_gps_breitengrad_value")
        self.l_gps_geschwindigkeit_value: QLabel = self.findChild(QLabel, "l_gps_geschwindigkeit_value")
        self.l_gps_time_value: QLabel = self.findChild(QLabel, "l_gps_time_value")
        self.l_gps_fix_value: QLabel = self.findChild(QLabel, "l_gps_fix_value")


        self.logging_enabled = False
        self.mcp9808_temperature = ""
        self.hp206_pressure = ""
        self.hp206_temperature = ""
        self.hp206_altitude = ""
        self.th02_temperature = ""
        self.th02_humidity = ""
        self.uv_index = ""
        self.tsl2591_light = ""
        self.ccs811_eco2 = ""
        self.ccs811_tvoc = ""
        self.sds011_pm25 = ""
        self.sds011_pm10 = ""
        self.gps_gpgga = ""
        self.gps_gprmc = ""
        self.sd = ""

        ports = QtSerialPort.QSerialPortInfo.availablePorts()
        for port in ports:
            self.cb_serial_ports.addItem(port.portName())

        self.b_connect_serial: QPushButton = self.findChild(QPushButton, "b_connect_serial")
        self.b_connect_serial.clicked.connect(self.b_confirm_handler)

        self.b_start_logging: QPushButton = self.findChild(QPushButton, "b_start_logging")
        self.b_start_logging.clicked.connect(self.b_logging_handler)

    def init_logfile(self):
        csvfile = open('log.csv', 'a')
        csvfile.write("TIMESTAMP;")
        csvfile.write("mcp9808_temperature;")
        csvfile.write("hp206_pressure;")
        csvfile.write("hp206_temperature;")
        csvfile.write("hp206_altitude;")
        csvfile.write("th02_temperature;")
        csvfile.write("th02_humidity;")
        csvfile.write("uv_index;")
        csvfile.write("tsl2591_light;")
        csvfile.write("ccs811_eco2;")
        csvfile.write("ccs811_tvoc;")
        csvfile.write("sds011_pm25;")
        csvfile.write("sds011_pm10;")
        csvfile.write("gps_data_gpgga;")
        csvfile.write("gps_data_gprmc;")
        csvfile.write("sd_status;\n")
        csvfile.close()
        

    @QtCore.Slot(bool)
    def b_confirm_handler(self, checked):
        
        self.serial = QtSerialPort.QSerialPort(
            self.cb_serial_ports.currentText(),
            baudRate=QtSerialPort.QSerialPort.Baud9600,
            readyRead=self.receive
        )
        self.b_connect_serial.setText("Disconnect" if checked else "Connect")
        if checked:
            if not self.serial.isOpen():
                if not self.serial.open(QtCore.QIODevice.ReadWrite):
                    self.b_connect_serial.setChecked(False)
        else:
            self.serial.close()

    @QtCore.Slot(bool)
    def b_logging_handler(self, checked):
        
        self.b_start_logging.setText("Stop logging" if checked else "Start logging")
        if checked:
            self.init_logfile()
            self.logging_enabled = True
        else:
            self.logging_enabled = False
        

    @QtCore.Slot()
    def receive(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.replace('\x00', "")
            text = text.replace('\r', "")
            text = text.replace('\n', "")
            self.pte_serial_console.appendPlainText(text)
            if "#!" in text and self.logging_enabled == True:
                self.csvstring = (str(datetime.datetime.now()) + ";" + 
                             self.mcp9808_temperature + ";" + 
                             self.hp206_pressure + ";" + 
                             self.hp206_temperature + ";" + 
                             self.hp206_altitude + ";" +
                             self.th02_temperature + ";" + 
                             self.th02_humidity + ";" + 
                             self.uv_index + ";" + 
                             self.tsl2591_light + ";" + 
                             self.ccs811_eco2 + ";" + 
                             self.ccs811_tvoc + ";" + 
                             self.sds011_pm25 + ";" + 
                             self.sds011_pm10 + ";" + 
                             self.gps_gpgga + ";" + 
                             self.gps_gprmc + ";" + 
                             self.sd + "\n"
                )
                
                with open("log.csv", "a") as csvfile:
                    csvfile.write(self.csvstring)
                
                self.mcp9808_temperature = ""
                self.hp206_pressure = ""
                self.hp206_temperature = ""
                self.hp206_altitude = ""
                self.th02_temperature = ""
                self.th02_humidity = ""
                self.uv_index = ""
                self.tsl2591_light = ""
                self.ccs811_eco2 = ""
                self.ccs811_tvoc = ""
                self.sds011_pm25 = ""
                self.sds011_pm10 = ""
                self.gps_gpgga = ""
                self.gps_gprmc = ""
                self.sd = ""

            if text.startswith("mcp9808_temperature"):
                self.mcp9808_temperature = text[text.index(':')+1: text.index(',')]        
                self.l_mcp9808_value.setText(self.mcp9808_temperature + "°C")
            if text.startswith("hp206_pressure"):
                self.hp206_pressure = text[text.index(':')+1: text.index(',')]
                self.l_hp206_pressure_value.setText(self.hp206_pressure + "hPa")
            if text.startswith("hp206_temperature"):
                self.hp206_temperature = text[text.index(':')+1: text.index(',')]
                self.l_hp206_temperature_value.setText(self.hp206_temperature + "°C")
            if text.startswith("hp206_altitude"):
                self.hp206_altitude = text[text.index(':')+1: text.index(',')]
                self.l_hp206_altitude_value.setText(self.hp206_altitude + "m")
            if text.startswith("th02_temperature"):
                self.th02_temperature = text[text.index(':')+1: text.index(',')]
                self.l_th02_temperature_value.setText(self.th02_temperature + "°C")
            if text.startswith("th02_humidity"):
                self.th02_humidity = text[text.index(':')+1: text.index(',')]
                self.l_th02_humidity_value.setText(self.th02_humidity + "%")
            if text.startswith("uv_index"):
                self.uv_index = text[text.index(':')+1: text.index(',')]
                self.l_uv_index_value.setText(self.uv_index)
            if text.startswith("tsl2591_light"):
                self.tsl2591_light = text[text.index(':')+1: text.index(',')]
                self.l_tsl2591_light_value.setText(self.tsl2591_light + " lux")
            if text.startswith("ccs811_eco2"):
                self.ccs811_eco2 = text[text.index(':')+1: text.index(',')]
                self.l_ccs811_eco2_value.setText(self.ccs811_eco2)
            if text.startswith("ccs811_tvoc"):
                self.ccs811_tvoc = text[text.index(':')+1: text.index(',')]
                self.l_ccs811_tvoc_value.setText(self.ccs811_tvoc)
            if text.startswith("sds011_pm25"):
                self.sds011_pm25 = text[text.index(':')+1: text.index(',')]
                self.l_sds011_pm25_value.setText(self.sds011_pm25)
            if text.startswith("sds011_pm10"):
                self.sds011_pm10 = text[text.index(':')+1: text.index(',')]
                self.l_sds011_pm10_value.setText(self.sds011_pm10)


            if text.startswith("$GPGGA"):
                self.gps_gpgga = text[0: text.index(", RSSI")]
                
                try:
                    self.gps_gpgga_nmeamessage: pynmeagps.NMEAMessage = pynmeagps.NMEAReader.parse(self.gps_gpgga)

                    self.l_gps_breitengrad_value.setText(self.gps_gpgga_nmeamessage.lat)
                    self.l_gps_laengengrad_value.setText(self.gps_gpgga_nmeamessage.lon)

                    self.gps_gpgga.split(',')

                    if (self.gps_gpgga.split(',')[6] == "0"):
                        self.l_gps_fix_value.setText("No fix")
                    if (self.gps_gpgga.split(',')[6] == "1"):
                        self.l_gps_fix_value.setText("GPS SPS Mode")
                    if (self.gps_gpgga.split(',')[6] == "2"):
                        self.l_gps_fix_value.setText("Diff GPS, SPS Mode")
                    if (self.gps_gpgga.split(',')[6] == "3"):
                        self.l_gps_fix_value.setText("PGS PPS ModeRo")
                except:
                    pass

                

            if text.startswith("$GPRMC"):
                self.gps_gprmc = text[0: text.index(", RSSI")]

                try:
                    self.gps_gprmc_nmeamessage: pynmeagps.NMEAMessage = pynmeagps.NMEAReader.parse(self.gps_gprmc)

                    self.l_gps_time_value.setText(self.gps_gprmc_nmeamessage.time.strftime("%H:%M:%S") + " UTC")
                    self.l_gps_geschwindigkeit_value.setText(self.gps_gprmc_nmeamessage.spd)
                except:
                    pass
            
            if text.startswith("SD"):
                self.sd = text[text.index(':')+1: text.index(',')]
                self.l_sd_value.setText(self.sd)



if __name__ == "__main__":
    try:
        if sys.argv[1]:
          os.chdir(sys.argv[1])
    except:
        pass


    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication()

    main = MainUI()
    main.show()
    sys.exit(app.exec())
    