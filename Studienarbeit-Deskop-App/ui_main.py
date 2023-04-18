# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1450, 592)
        self.l_SerialPort = QLabel(Form)
        self.l_SerialPort.setObjectName(u"l_SerialPort")
        self.l_SerialPort.setGeometry(QRect(500, 490, 61, 16))
        self.pte_serial_console = QPlainTextEdit(Form)
        self.pte_serial_console.setObjectName(u"pte_serial_console")
        self.pte_serial_console.setGeometry(QRect(20, 410, 461, 151))
        self.pte_serial_console.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.b_connect_serial = QPushButton(Form)
        self.b_connect_serial.setObjectName(u"b_connect_serial")
        self.b_connect_serial.setGeometry(QRect(640, 530, 75, 24))
        self.b_connect_serial.setCheckable(True)
        self.cb_serial_ports = QComboBox(Form)
        self.cb_serial_ports.setObjectName(u"cb_serial_ports")
        self.cb_serial_ports.setGeometry(QRect(570, 490, 141, 21))
        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 10, 961, 391))
        self.gridLayout_12 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.l_hp206 = QLabel(self.gridLayoutWidget_2)
        self.l_hp206.setObjectName(u"l_hp206")
        font = QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.l_hp206.setFont(font)
        self.l_hp206.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.l_hp206)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.l_hp206_temperature_value = QLabel(self.gridLayoutWidget_2)
        self.l_hp206_temperature_value.setObjectName(u"l_hp206_temperature_value")
        font1 = QFont()
        font1.setPointSize(12)
        self.l_hp206_temperature_value.setFont(font1)
        self.l_hp206_temperature_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l_hp206_temperature_value, 1, 1, 1, 1)

        self.l_hp206_altitude = QLabel(self.gridLayoutWidget_2)
        self.l_hp206_altitude.setObjectName(u"l_hp206_altitude")
        self.l_hp206_altitude.setFont(font1)

        self.gridLayout_3.addWidget(self.l_hp206_altitude, 2, 0, 1, 1)

        self.l_hp206_temperature = QLabel(self.gridLayoutWidget_2)
        self.l_hp206_temperature.setObjectName(u"l_hp206_temperature")
        self.l_hp206_temperature.setFont(font1)

        self.gridLayout_3.addWidget(self.l_hp206_temperature, 1, 0, 1, 1)

        self.l_hp206_altitude_value = QLabel(self.gridLayoutWidget_2)
        self.l_hp206_altitude_value.setObjectName(u"l_hp206_altitude_value")
        self.l_hp206_altitude_value.setFont(font1)
        self.l_hp206_altitude_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l_hp206_altitude_value, 2, 1, 1, 1)

        self.l_hp206_pressure_value = QLabel(self.gridLayoutWidget_2)
        self.l_hp206_pressure_value.setObjectName(u"l_hp206_pressure_value")
        self.l_hp206_pressure_value.setFont(font1)
        self.l_hp206_pressure_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l_hp206_pressure_value, 0, 1, 1, 1)

        self.l_hp206_pressure = QLabel(self.gridLayoutWidget_2)
        self.l_hp206_pressure.setObjectName(u"l_hp206_pressure")
        self.l_hp206_pressure.setFont(font1)

        self.gridLayout_3.addWidget(self.l_hp206_pressure, 0, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_3)


        self.gridLayout_12.addLayout(self.verticalLayout_6, 0, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.l_mcp9808 = QLabel(self.gridLayoutWidget_2)
        self.l_mcp9808.setObjectName(u"l_mcp9808")
        self.l_mcp9808.setFont(font)
        self.l_mcp9808.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.l_mcp9808)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.l_mcp9808_value = QLabel(self.gridLayoutWidget_2)
        self.l_mcp9808_value.setObjectName(u"l_mcp9808_value")
        self.l_mcp9808_value.setFont(font1)
        self.l_mcp9808_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.l_mcp9808_value, 0, 1, 1, 1)

        self.l_mcp9808_temperatur = QLabel(self.gridLayoutWidget_2)
        self.l_mcp9808_temperatur.setObjectName(u"l_mcp9808_temperatur")
        self.l_mcp9808_temperatur.setFont(font1)

        self.gridLayout_13.addWidget(self.l_mcp9808_temperatur, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_13.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_13.addWidget(self.label_4, 2, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_13)


        self.gridLayout_12.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.l_uv = QLabel(self.gridLayoutWidget_2)
        self.l_uv.setObjectName(u"l_uv")
        self.l_uv.setFont(font)
        self.l_uv.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.l_uv)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.l_uv_index = QLabel(self.gridLayoutWidget_2)
        self.l_uv_index.setObjectName(u"l_uv_index")
        self.l_uv_index.setFont(font1)

        self.gridLayout_14.addWidget(self.l_uv_index, 0, 0, 1, 1)

        self.l_uv_index_value = QLabel(self.gridLayoutWidget_2)
        self.l_uv_index_value.setObjectName(u"l_uv_index_value")
        self.l_uv_index_value.setFont(font1)
        self.l_uv_index_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.l_uv_index_value, 0, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_14.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_14.addWidget(self.label_6, 2, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_14)


        self.gridLayout_12.addLayout(self.verticalLayout_8, 1, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.l_tsl2591 = QLabel(self.gridLayoutWidget_2)
        self.l_tsl2591.setObjectName(u"l_tsl2591")
        self.l_tsl2591.setFont(font)
        self.l_tsl2591.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.l_tsl2591)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.l_tsl2591_light = QLabel(self.gridLayoutWidget_2)
        self.l_tsl2591_light.setObjectName(u"l_tsl2591_light")
        self.l_tsl2591_light.setFont(font1)

        self.gridLayout_15.addWidget(self.l_tsl2591_light, 0, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_15.addWidget(self.label_8, 1, 1, 1, 1)

        self.l_tsl2591_light_value = QLabel(self.gridLayoutWidget_2)
        self.l_tsl2591_light_value.setObjectName(u"l_tsl2591_light_value")
        self.l_tsl2591_light_value.setFont(font1)
        self.l_tsl2591_light_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.l_tsl2591_light_value, 0, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_15.addWidget(self.label_9, 2, 1, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_15)


        self.gridLayout_12.addLayout(self.verticalLayout_9, 1, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.l_th02 = QLabel(self.gridLayoutWidget_2)
        self.l_th02.setObjectName(u"l_th02")
        self.l_th02.setFont(font)
        self.l_th02.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.l_th02)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.l_th02_humidity = QLabel(self.gridLayoutWidget_2)
        self.l_th02_humidity.setObjectName(u"l_th02_humidity")
        self.l_th02_humidity.setFont(font1)

        self.gridLayout_4.addWidget(self.l_th02_humidity, 0, 0, 1, 1)

        self.l_th02_temperature_value = QLabel(self.gridLayoutWidget_2)
        self.l_th02_temperature_value.setObjectName(u"l_th02_temperature_value")
        self.l_th02_temperature_value.setFont(font1)
        self.l_th02_temperature_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l_th02_temperature_value, 1, 1, 1, 1)

        self.l_th02_temperature = QLabel(self.gridLayoutWidget_2)
        self.l_th02_temperature.setObjectName(u"l_th02_temperature")
        self.l_th02_temperature.setFont(font1)

        self.gridLayout_4.addWidget(self.l_th02_temperature, 1, 0, 1, 1)

        self.l_th02_humidity_value = QLabel(self.gridLayoutWidget_2)
        self.l_th02_humidity_value.setObjectName(u"l_th02_humidity_value")
        self.l_th02_humidity_value.setFont(font1)
        self.l_th02_humidity_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l_th02_humidity_value, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_4)


        self.gridLayout_12.addLayout(self.verticalLayout_7, 0, 2, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.l_sds011 = QLabel(self.gridLayoutWidget_2)
        self.l_sds011.setObjectName(u"l_sds011")
        self.l_sds011.setFont(font)
        self.l_sds011.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.l_sds011)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.l_sds011_pm10_value = QLabel(self.gridLayoutWidget_2)
        self.l_sds011_pm10_value.setObjectName(u"l_sds011_pm10_value")
        self.l_sds011_pm10_value.setFont(font1)
        self.l_sds011_pm10_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.l_sds011_pm10_value, 1, 1, 1, 1)

        self.l_sds011_pm10 = QLabel(self.gridLayoutWidget_2)
        self.l_sds011_pm10.setObjectName(u"l_sds011_pm10")
        self.l_sds011_pm10.setFont(font1)

        self.gridLayout_6.addWidget(self.l_sds011_pm10, 1, 0, 1, 1)

        self.l_sds011_pm25_value = QLabel(self.gridLayoutWidget_2)
        self.l_sds011_pm25_value.setObjectName(u"l_sds011_pm25_value")
        self.l_sds011_pm25_value.setFont(font1)
        self.l_sds011_pm25_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.l_sds011_pm25_value, 0, 1, 1, 1)

        self.l_sds011_pm25 = QLabel(self.gridLayoutWidget_2)
        self.l_sds011_pm25.setObjectName(u"l_sds011_pm25")
        self.l_sds011_pm25.setFont(font1)

        self.gridLayout_6.addWidget(self.l_sds011_pm25, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 2, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_6)


        self.gridLayout_12.addLayout(self.verticalLayout_11, 2, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.l_ccs811 = QLabel(self.gridLayoutWidget_2)
        self.l_ccs811.setObjectName(u"l_ccs811")
        self.l_ccs811.setFont(font)
        self.l_ccs811.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.l_ccs811)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.l_ccs811_tvoc_value = QLabel(self.gridLayoutWidget_2)
        self.l_ccs811_tvoc_value.setObjectName(u"l_ccs811_tvoc_value")
        self.l_ccs811_tvoc_value.setFont(font1)
        self.l_ccs811_tvoc_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.l_ccs811_tvoc_value, 1, 1, 1, 1)

        self.l_ccs811_eco2_value = QLabel(self.gridLayoutWidget_2)
        self.l_ccs811_eco2_value.setObjectName(u"l_ccs811_eco2_value")
        self.l_ccs811_eco2_value.setFont(font1)
        self.l_ccs811_eco2_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.l_ccs811_eco2_value, 0, 1, 1, 1)

        self.l_ccs811_tvoc = QLabel(self.gridLayoutWidget_2)
        self.l_ccs811_tvoc.setObjectName(u"l_ccs811_tvoc")
        self.l_ccs811_tvoc.setFont(font1)

        self.gridLayout_5.addWidget(self.l_ccs811_tvoc, 1, 0, 1, 1)

        self.l_ccs811_eco2 = QLabel(self.gridLayoutWidget_2)
        self.l_ccs811_eco2.setObjectName(u"l_ccs811_eco2")
        self.l_ccs811_eco2.setFont(font1)

        self.gridLayout_5.addWidget(self.l_ccs811_eco2, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_5)


        self.gridLayout_12.addLayout(self.verticalLayout_10, 2, 1, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.l_gps = QLabel(self.gridLayoutWidget_2)
        self.l_gps.setObjectName(u"l_gps")
        self.l_gps.setFont(font)
        self.l_gps.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.l_gps)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.l_gps_breitengrad_value = QLabel(self.gridLayoutWidget_2)
        self.l_gps_breitengrad_value.setObjectName(u"l_gps_breitengrad_value")
        self.l_gps_breitengrad_value.setFont(font1)
        self.l_gps_breitengrad_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.l_gps_breitengrad_value, 1, 1, 1, 1)

        self.l_gps_breitengrad = QLabel(self.gridLayoutWidget_2)
        self.l_gps_breitengrad.setObjectName(u"l_gps_breitengrad")
        self.l_gps_breitengrad.setFont(font1)

        self.gridLayout_17.addWidget(self.l_gps_breitengrad, 1, 0, 1, 1)

        self.l_gps_laengengrad_value = QLabel(self.gridLayoutWidget_2)
        self.l_gps_laengengrad_value.setObjectName(u"l_gps_laengengrad_value")
        self.l_gps_laengengrad_value.setFont(font1)
        self.l_gps_laengengrad_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.l_gps_laengengrad_value, 0, 1, 1, 1)

        self.l_gps_laengengrad = QLabel(self.gridLayoutWidget_2)
        self.l_gps_laengengrad.setObjectName(u"l_gps_laengengrad")
        self.l_gps_laengengrad.setFont(font1)

        self.gridLayout_17.addWidget(self.l_gps_laengengrad, 0, 0, 1, 1)

        self.l_gps_time = QLabel(self.gridLayoutWidget_2)
        self.l_gps_time.setObjectName(u"l_gps_time")
        self.l_gps_time.setFont(font1)

        self.gridLayout_17.addWidget(self.l_gps_time, 2, 0, 1, 1)

        self.l_gps_time_value = QLabel(self.gridLayoutWidget_2)
        self.l_gps_time_value.setObjectName(u"l_gps_time_value")
        self.l_gps_time_value.setFont(font1)
        self.l_gps_time_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.l_gps_time_value, 2, 1, 1, 1)


        self.verticalLayout_24.addLayout(self.gridLayout_17)


        self.gridLayout_12.addLayout(self.verticalLayout_24, 1, 2, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.l_gps_geschwindigkeit = QLabel(self.gridLayoutWidget_2)
        self.l_gps_geschwindigkeit.setObjectName(u"l_gps_geschwindigkeit")
        self.l_gps_geschwindigkeit.setFont(font1)

        self.gridLayout_18.addWidget(self.l_gps_geschwindigkeit, 0, 0, 1, 1)

        self.l_gps_fix_value = QLabel(self.gridLayoutWidget_2)
        self.l_gps_fix_value.setObjectName(u"l_gps_fix_value")
        self.l_gps_fix_value.setFont(font1)
        self.l_gps_fix_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.l_gps_fix_value, 1, 1, 1, 1)

        self.l_gps_fix = QLabel(self.gridLayoutWidget_2)
        self.l_gps_fix.setObjectName(u"l_gps_fix")
        self.l_gps_fix.setFont(font1)

        self.gridLayout_18.addWidget(self.l_gps_fix, 1, 0, 1, 1)

        self.l_gps_geschwindigkeit_value = QLabel(self.gridLayoutWidget_2)
        self.l_gps_geschwindigkeit_value.setObjectName(u"l_gps_geschwindigkeit_value")
        self.l_gps_geschwindigkeit_value.setFont(font1)
        self.l_gps_geschwindigkeit_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.l_gps_geschwindigkeit_value, 0, 1, 1, 1)

        self.l_gps_time_value_3 = QLabel(self.gridLayoutWidget_2)
        self.l_gps_time_value_3.setObjectName(u"l_gps_time_value_3")
        self.l_gps_time_value_3.setFont(font1)
        self.l_gps_time_value_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.l_gps_time_value_3, 2, 0, 1, 1)

        self.l_gps_time_value_2 = QLabel(self.gridLayoutWidget_2)
        self.l_gps_time_value_2.setObjectName(u"l_gps_time_value_2")
        self.l_gps_time_value_2.setFont(font1)
        self.l_gps_time_value_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.l_gps_time_value_2, 3, 1, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_18, 2, 2, 1, 1)

        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(560, 420, 151, 60))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.l_sd = QLabel(self.verticalLayoutWidget)
        self.l_sd.setObjectName(u"l_sd")
        self.l_sd.setFont(font)
        self.l_sd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.l_sd)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.l_sd_value = QLabel(self.verticalLayoutWidget)
        self.l_sd_value.setObjectName(u"l_sd_value")
        self.l_sd_value.setFont(font1)
        self.l_sd_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.l_sd_value, 0, 1, 1, 1)

        self.l_sd_status = QLabel(self.verticalLayoutWidget)
        self.l_sd_status.setObjectName(u"l_sd_status")
        self.l_sd_status.setFont(font1)

        self.gridLayout_16.addWidget(self.l_sd_status, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_16)

        self.b_start_logging = QPushButton(Form)
        self.b_start_logging.setObjectName(u"b_start_logging")
        self.b_start_logging.setGeometry(QRect(750, 430, 91, 24))
        self.b_start_logging.setCheckable(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.l_SerialPort.setText(QCoreApplication.translate("Form", u"Serial Port:", None))
        self.b_connect_serial.setText(QCoreApplication.translate("Form", u"Connect", None))
        self.l_hp206.setText(QCoreApplication.translate("Form", u"HP206", None))
        self.l_hp206_temperature_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_hp206_altitude.setText(QCoreApplication.translate("Form", u"Gemessene H\u00f6he:", None))
        self.l_hp206_temperature.setText(QCoreApplication.translate("Form", u"Temperatur:", None))
        self.l_hp206_altitude_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_hp206_pressure_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_hp206_pressure.setText(QCoreApplication.translate("Form", u"Luftdruck:", None))
        self.l_mcp9808.setText(QCoreApplication.translate("Form", u"MCP9808", None))
        self.l_mcp9808_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_mcp9808_temperatur.setText(QCoreApplication.translate("Form", u"Temperatur:", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.l_uv.setText(QCoreApplication.translate("Form", u"UV", None))
        self.l_uv_index.setText(QCoreApplication.translate("Form", u"Index:", None))
        self.l_uv_index_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_5.setText("")
        self.label_6.setText("")
        self.l_tsl2591.setText(QCoreApplication.translate("Form", u"TSL2591", None))
        self.l_tsl2591_light.setText(QCoreApplication.translate("Form", u"Lichtintensit\u00e4t:", None))
        self.label_8.setText("")
        self.l_tsl2591_light_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_9.setText("")
        self.l_th02.setText(QCoreApplication.translate("Form", u"TH02", None))
        self.l_th02_humidity.setText(QCoreApplication.translate("Form", u"Luftfeuchtigkeit:", None))
        self.l_th02_temperature_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_th02_temperature.setText(QCoreApplication.translate("Form", u"Temperatur:", None))
        self.l_th02_humidity_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.label.setText("")
        self.l_sds011.setText(QCoreApplication.translate("Form", u"SDS011", None))
        self.l_sds011_pm10_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_sds011_pm10.setText(QCoreApplication.translate("Form", u"PM10:", None))
        self.l_sds011_pm25_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_sds011_pm25.setText(QCoreApplication.translate("Form", u"PM2.5:", None))
        self.label_2.setText("")
        self.l_ccs811.setText(QCoreApplication.translate("Form", u"CCS811", None))
        self.l_ccs811_tvoc_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_ccs811_eco2_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_ccs811_tvoc.setText(QCoreApplication.translate("Form", u"TVOC:", None))
        self.l_ccs811_eco2.setText(QCoreApplication.translate("Form", u"eCO\u00b2:", None))
        self.label_7.setText("")
        self.l_gps.setText(QCoreApplication.translate("Form", u"GPS", None))
        self.l_gps_breitengrad_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_gps_breitengrad.setText(QCoreApplication.translate("Form", u"Breitengrad:", None))
        self.l_gps_laengengrad_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_gps_laengengrad.setText(QCoreApplication.translate("Form", u"L\u00e4ngengrad", None))
        self.l_gps_time.setText(QCoreApplication.translate("Form", u"Time:", None))
        self.l_gps_time_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_gps_geschwindigkeit.setText(QCoreApplication.translate("Form", u"Geschwindigket:", None))
        self.l_gps_fix_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_gps_fix.setText(QCoreApplication.translate("Form", u"GPS Fix:", None))
        self.l_gps_geschwindigkeit_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_gps_time_value_3.setText("")
        self.l_gps_time_value_2.setText("")
        self.l_sd.setText(QCoreApplication.translate("Form", u"SD Card", None))
        self.l_sd_value.setText(QCoreApplication.translate("Form", u"-", None))
        self.l_sd_status.setText(QCoreApplication.translate("Form", u"Status:", None))
        self.b_start_logging.setText(QCoreApplication.translate("Form", u"Start logging", None))
    # retranslateUi

