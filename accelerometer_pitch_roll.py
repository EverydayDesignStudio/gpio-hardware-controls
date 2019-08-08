#!/usr/bin/env python3

import sys
import time
import math
import RPi.GPIO as GPIO

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)


def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()

write("--- ADXL337 Accelerometer with MCP3008 ---")

try:
    while True:
        # acc_values = [round(x, 2) for x in motion.accelerometer()]
        # ax = acc_values[0]
        # ay = acc_values[1]
        # az = acc_values[2]
        
        #print('Raw ADC Value: ', chan.value)
        #print('Chan1: ', chan1.value)
        #print('Chan2: ', chan2.value)
        #print('Chan3: ', chan3.value)
        #print('Chan4: ', chan4.value)
        
        chan0 = AnalogIn(mcp, MCP.P0)
        chan1 = AnalogIn(mcp, MCP.P2)
        chan2 = AnalogIn(mcp, MCP.P4)
        ax = chan0.value
        ay = chan1.value
        az = chan2.value
        
        pitch = 180 * math.atan(ax/math.sqrt(ay*ay + az*az))/math.pi
        roll = 180 * math.atan(ay/math.sqrt(ax*ax + az*az))/math.pi
        
        #if roll > -45 and roll < 45:
        #    orientation = 'landscape'
        #elif roll >= 45 or roll <= -45:
        #    orientation = 'vertical'
        
        if pitch > 35 and roll < 34:
                orientation = 'correct vertical'
        elif pitch < 31 and roll > 34:
                orientation = 'upside down vertical'
        else:
                orientation = 'horizontal'

        output = """
Accelerometer: {x}g {y}g {z}g

Pitch: {p}
Roll: {r}

Orientation: {o}

""".format(
            x=ax,
            y=ay,
            z=az,
            p = pitch,
            r = roll,
            o = orientation
        )

        output = output.replace("\n", "\n\033[K")
        write(output)
        lines = len(output.split("\n"))
        write("\033[{}A".format(lines - 1))

        time.sleep(.1)

except KeyboardInterrupt:
    pass
