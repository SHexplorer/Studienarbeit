# Studienarbeit

This Repo is contains all source files for the Sensorkit Desktop App, Main Controller, CoProcessor and Receiver and PCB files. The Sensorkit is a university project with the title "Modification of a quadrocopter for the acquisition of meteorological data", made by two german students.

The final Thesis is stored as Studienarbeit.pdf.

## Main Controller ##

Based on PlatformIO

Notes: The following line of the MCP9808 library had to be adapted for compatibility with the atmel32u4:

change `#define WIRE Wire1` to `#define WIRE Wire`

## CoProcessor ##

Based on PlatformIO

## Receiver ##

Based on PlatformIO

## Desktop App ##

Based on python with QT Framework (PySide6)

## PCB ##

The PCB is made with EasyEDA and ordered by JLCPCB.

***CAUTION***

The PCB has some major design mistakes and should not be used out of the box:
- labeling for power connetor is wrong
- wrong footprint for 18650 battery
- careful when using em-406a GPS - Cable had to be twistet for right pins 

Things that should be added:
- USB connector for charging indstead of the clamp connector
- On/Off switch