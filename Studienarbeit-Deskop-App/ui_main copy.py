# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main copy.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(773, 601)
        self.l_SerialPort = QLabel(Form)
        self.l_SerialPort.setObjectName(u"l_SerialPort")
        self.l_SerialPort.setGeometry(QRect(500, 530, 61, 16))
        self.pte_serial_console = QPlainTextEdit(Form)
        self.pte_serial_console.setObjectName(u"pte_serial_console")
        self.pte_serial_console.setGeometry(QRect(20, 430, 461, 151))
        self.pte_serial_console.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.b_connect_serial = QPushButton(Form)
        self.b_connect_serial.setObjectName(u"b_connect_serial")
        self.b_connect_serial.setGeometry(QRect(660, 560, 75, 24))
        self.b_connect_serial.setCheckable(True)
        self.cb_serial_ports = QComboBox(Form)
        self.cb_serial_ports.setObjectName(u"cb_serial_ports")
        self.cb_serial_ports.setGeometry(QRect(590, 530, 141, 21))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(590, 430, 141, 80))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.l_sd = QLabel(self.verticalLayoutWidget)
        self.l_sd.setObjectName(u"l_sd")
        font = QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.l_sd.setFont(font)
        self.l_sd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.l_sd)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.l_sd_status = QLabel(self.verticalLayoutWidget)
        self.l_sd_status.setObjectName(u"l_sd_status")
        font1 = QFont()
        font1.setPointSize(12)
        self.l_sd_status.setFont(font1)

        self.horizontalLayout.addWidget(self.l_sd_status)

        self.l_sd_value = QLabel(self.verticalLayoutWidget)
        self.l_sd_value.setObjectName(u"l_sd_value")
        self.l_sd_value.setFont(font1)
        self.l_sd_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.l_sd_value)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 20, 141, 80))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.l_mcp9808 = QLabel(self.verticalLayoutWidget_2)
        self.l_mcp9808.setObjectName(u"l_mcp9808")
        self.l_mcp9808.setFont(font)
        self.l_mcp9808.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.l_mcp9808)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.l_mcp9808_temperatur = QLabel(self.verticalLayoutWidget_2)
        self.l_mcp9808_temperatur.setObjectName(u"l_mcp9808_temperatur")
        self.l_mcp9808_temperatur.setFont(font1)

        self.horizontalLayout_2.addWidget(self.l_mcp9808_temperatur)

        self.l_mcp9808_value = QLabel(self.verticalLayoutWidget_2)
        self.l_mcp9808_value.setObjectName(u"l_mcp9808_value")
        self.l_mcp9808_value.setFont(font1)
        self.l_mcp9808_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.l_mcp9808_value)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayoutWidget_3 = QWidget(Form)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(190, 20, 221, 116))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.l_hp206 = QLabel(self.verticalLayoutWidget_3)
        self.l_hp206.setObjectName(u"l_hp206")
        self.l_hp206.setFont(font)
        self.l_hp206.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.l_hp206)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.l_hp206_temperature_value = QLabel(self.verticalLayoutWidget_3)
        self.l_hp206_temperature_value.setObjectName(u"l_hp206_temperature_value")
        self.l_hp206_temperature_value.setFont(font1)
        self.l_hp206_temperature_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l_hp206_temperature_value, 1, 1, 1, 1)

        self.l_hp206_pressure = QLabel(self.verticalLayoutWidget_3)
        self.l_hp206_pressure.setObjectName(u"l_hp206_pressure")
        self.l_hp206_pressure.setFont(font1)

        self.gridLayout_3.addWidget(self.l_hp206_pressure, 0, 0, 1, 1)

        self.l_hp206_temperature = QLabel(self.verticalLayoutWidget_3)
        self.l_hp206_temperature.setObjectName(u"l_hp206_temperature")
        self.l_hp206_temperature.setFont(font1)

        self.gridLayout_3.addWidget(self.l_hp206_temperature, 1, 0, 1, 1)

        self.l_hp206_pressure_value = QLabel(self.verticalLayoutWidget_3)
        self.l_hp206_pressure_value.setObjectName(u"l_hp206_pressure_value")
        self.l_hp206_pressure_value.setFont(font1)
        self.l_hp206_pressure_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l_hp206_pressure_value, 0, 1, 1, 1)

        self.l_hp206_altitude = QLabel(self.verticalLayoutWidget_3)
        self.l_hp206_altitude.setObjectName(u"l_hp206_altitude")
        self.l_hp206_altitude.setFont(font1)

        self.gridLayout_3.addWidget(self.l_hp206_altitude, 2, 0, 1, 1)

        self.l_hp206_altitude_value = QLabel(self.verticalLayoutWidget_3)
        self.l_hp206_altitude_value.setObjectName(u"l_hp206_altitude_value")
        self.l_hp206_altitude_value.setFont(font1)
        self.l_hp206_altitude_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l_hp206_altitude_value, 2, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_3)

        self.verticalLayoutWidget_4 = QWidget(Form)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(440, 20, 221, 116))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.l_th02 = QLabel(self.verticalLayoutWidget_4)
        self.l_th02.setObjectName(u"l_th02")
        self.l_th02.setFont(font)
        self.l_th02.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.l_th02)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.l_th02_humidity = QLabel(self.verticalLayoutWidget_4)
        self.l_th02_humidity.setObjectName(u"l_th02_humidity")
        self.l_th02_humidity.setFont(font1)

        self.gridLayout_4.addWidget(self.l_th02_humidity, 0, 0, 1, 1)

        self.l_th02_temperature_value = QLabel(self.verticalLayoutWidget_4)
        self.l_th02_temperature_value.setObjectName(u"l_th02_temperature_value")
        self.l_th02_temperature_value.setFont(font1)
        self.l_th02_temperature_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l_th02_temperature_value, 1, 1, 1, 1)

        self.l_th02_temperature = QLabel(self.verticalLayoutWidget_4)
        self.l_th02_temperature.setObjectName(u"l_th02_temperature")
        self.l_th02_temperature.setFont(font1)

        self.gridLayout_4.addWidget(self.l_th02_temperature, 1, 0, 1, 1)

        self.l_th02_humidity_value = QLabel(self.verticalLayoutWidget_4)
        self.l_th02_humidity_value.setObjectName(u"l_th02_humidity_value")
        self.l_th02_humidity_value.setFont(font1)
        self.l_th02_humidity_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l_th02_humidity_value, 0, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_4)

        self.verticalLayoutWidget_5 = QWidget(Form)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(20, 170, 141, 80))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.l_uv = QLabel(self.verticalLayoutWidget_5)
        self.l_uv.setObjectName(u"l_uv")
        self.l_uv.setFont(font)
        self.l_uv.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.l_uv)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.l_uv_index = QLabel(self.verticalLayoutWidget_5)
        self.l_uv_index.setObjectName(u"l_uv_index")
        self.l_uv_index.setFont(font1)

        self.horizontalLayout_3.addWidget(self.l_uv_index)

        self.l_uv_index_value = QLabel(self.verticalLayoutWidget_5)
        self.l_uv_index_value.setObjectName(u"l_uv_index_value")
        self.l_uv_index_value.setFont(font1)
        self.l_uv_index_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.l_uv_index_value)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.verticalLayoutWidget_6 = QWidget(Form)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(210, 170, 191, 80))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.l_tsl2591 = QLabel(self.verticalLayoutWidget_6)
        self.l_tsl2591.setObjectName(u"l_tsl2591")
        self.l_tsl2591.setFont(font)
        self.l_tsl2591.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.l_tsl2591)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.l_tsl2591_light = QLabel(self.verticalLayoutWidget_6)
        self.l_tsl2591_light.setObjectName(u"l_tsl2591_light")
        self.l_tsl2591_light.setFont(font1)

        self.horizontalLayout_4.addWidget(self.l_tsl2591_light)

        self.l_tsl2591_light_value = QLabel(self.verticalLayoutWidget_6)
        self.l_tsl2591_light_value.setObjectName(u"l_tsl2591_light_value")
        self.l_tsl2591_light_value.setFont(font1)
        self.l_tsl2591_light_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.l_tsl2591_light_value)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.verticalLayoutWidget_7 = QWidget(Form)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(230, 270, 151, 116))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.l_ccs811 = QLabel(self.verticalLayoutWidget_7)
        self.l_ccs811.setObjectName(u"l_ccs811")
        self.l_ccs811.setFont(font)
        self.l_ccs811.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.l_ccs811)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.l_ccs811_eco2 = QLabel(self.verticalLayoutWidget_7)
        self.l_ccs811_eco2.setObjectName(u"l_ccs811_eco2")
        self.l_ccs811_eco2.setFont(font1)

        self.gridLayout_5.addWidget(self.l_ccs811_eco2, 0, 0, 1, 1)

        self.l_ccs811_tvoc_value = QLabel(self.verticalLayoutWidget_7)
        self.l_ccs811_tvoc_value.setObjectName(u"l_ccs811_tvoc_value")
        self.l_ccs811_tvoc_value.setFont(font1)
        self.l_ccs811_tvoc_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.l_ccs811_tvoc_value, 1, 1, 1, 1)

        self.l_ccs811_tvoc = QLabel(self.verticalLayoutWidget_7)
        self.l_ccs811_tvoc.setObjectName(u"l_ccs811_tvoc")
        self.l_ccs811_tvoc.setFont(font1)

        self.gridLayout_5.addWidget(self.l_ccs811_tvoc, 1, 0, 1, 1)

        self.l_ccs811_eco2_value = QLabel(self.verticalLayoutWidget_7)
        self.l_ccs811_eco2_value.setObjectName(u"l_ccs811_eco2_value")
        self.l_ccs811_eco2_value.setFont(font1)
        self.l_ccs811_eco2_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.l_ccs811_eco2_value, 0, 1, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_5)

        self.verticalLayoutWidget_8 = QWidget(Form)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(20, 270, 131, 116))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.l_sds011 = QLabel(self.verticalLayoutWidget_8)
        self.l_sds011.setObjectName(u"l_sds011")
        self.l_sds011.setFont(font)
        self.l_sds011.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.l_sds011)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.l_sds011_pm25 = QLabel(self.verticalLayoutWidget_8)
        self.l_sds011_pm25.setObjectName(u"l_sds011_pm25")
        self.l_sds011_pm25.setFont(font1)

        self.gridLayout_6.addWidget(self.l_sds011_pm25, 0, 0, 1, 1)

        self.l_sds011_pm10_value = QLabel(self.verticalLayoutWidget_8)
        self.l_sds011_pm10_value.setObjectName(u"l_sds011_pm10_value")
        self.l_sds011_pm10_value.setFont(font1)
        self.l_sds011_pm10_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.l_sds011_pm10_value, 1, 1, 1, 1)

        self.l_sds011_pm10 = QLabel(self.verticalLayoutWidget_8)
        self.l_sds011_pm10.setObjectName(u"l_sds011_pm10")
        self.l_sds011_pm10.setFont(font1)

        self.gridLayout_6.addWidget(self.l_sds011_pm10, 1, 0, 1, 1)

        self.l_sds011_pm25_value = QLabel(self.verticalLayoutWidget_8)
        self.l_sds011_pm25_value.setObjectName(u"l_sds011_pm25_value")
        self.l_sds011_pm25_value.setFont(font1)
        self.l_sds011_pm25_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.l_sds011_pm25_value, 0, 1, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.l_SerialPort.setText(QCoreApplication.translate("Form", u"Serial Port:", None))
        self.b_connect_serial.setText(QCoreApplication.translate("Form", u"Connect", None))
        self.l_sd.setText(QCoreApplication.translate("Form", u"SD Card", None))
        self.l_sd_status.setText(QCoreApplication.translate("Form", u"Status:", None))
        self.l_sd_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_mcp9808.setText(QCoreApplication.translate("Form", u"MCP9808", None))
        self.l_mcp9808_temperatur.setText(QCoreApplication.translate("Form", u"Temperatur:", None))
        self.l_mcp9808_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_hp206.setText(QCoreApplication.translate("Form", u"HP206", None))
        self.l_hp206_temperature_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_hp206_pressure.setText(QCoreApplication.translate("Form", u"Luftdruck:", None))
        self.l_hp206_temperature.setText(QCoreApplication.translate("Form", u"Temperatur:", None))
        self.l_hp206_pressure_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_hp206_altitude.setText(QCoreApplication.translate("Form", u"berechnete H\u00f6he:", None))
        self.l_hp206_altitude_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_th02.setText(QCoreApplication.translate("Form", u"TH02", None))
        self.l_th02_humidity.setText(QCoreApplication.translate("Form", u"Luftfeuchtigkeit:", None))
        self.l_th02_temperature_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_th02_temperature.setText(QCoreApplication.translate("Form", u"Temperatur:", None))
        self.l_th02_humidity_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_uv.setText(QCoreApplication.translate("Form", u"UV", None))
        self.l_uv_index.setText(QCoreApplication.translate("Form", u"Index:", None))
        self.l_uv_index_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_tsl2591.setText(QCoreApplication.translate("Form", u"TSL2591", None))
        self.l_tsl2591_light.setText(QCoreApplication.translate("Form", u"Lichtintensit\u00e4t:", None))
        self.l_tsl2591_light_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_ccs811.setText(QCoreApplication.translate("Form", u"CCS811", None))
        self.l_ccs811_eco2.setText(QCoreApplication.translate("Form", u"eCO\u00b2:", None))
        self.l_ccs811_tvoc_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_ccs811_tvoc.setText(QCoreApplication.translate("Form", u"TVOC:", None))
        self.l_ccs811_eco2_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_sds011.setText(QCoreApplication.translate("Form", u"SDS011", None))
        self.l_sds011_pm25.setText(QCoreApplication.translate("Form", u"PM2.5:", None))
        self.l_sds011_pm10_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_sds011_pm10.setText(QCoreApplication.translate("Form", u"PM10:", None))
        self.l_sds011_pm25_value.setText(QCoreApplication.translate("Form", u"-", None))
    # retranslateUi

