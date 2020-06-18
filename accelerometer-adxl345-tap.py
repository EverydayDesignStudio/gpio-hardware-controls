#!/usr/bin/env python3

# Tap detection test for ADXL345 Accelerometer from Adafruit
# https://github.com/adafruit/Adafruit_CircuitPython_ADXL34x/blob/master/examples/adxl34x_tap_detection_test.py


import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)

# For ADXL343
# accelerometer = adafruit_adxl34x.ADXL343(i2c)
# For ADXL345
accelerometer = adafruit_adxl34x.ADXL345(i2c)

# you can also configure the tap detection parameters when you enable tap detection:
# accelerometer.enable_tap_detection(tap_count=2,threshold=20, duration=50)
# higher the threshold, harder the tap needs to be
accelerometer.enable_tap_detection(tap_count=1, threshold=150, duration=100)

while True:
    print("%f %f %f" % accelerometer.acceleration)

    print("Tapped: %s" % accelerometer.events["tap"])
    time.sleep(0.5)
