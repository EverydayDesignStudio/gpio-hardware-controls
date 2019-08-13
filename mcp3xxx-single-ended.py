#!/usr/bin/env python3

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import sys

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D8) # BCM 8 (CEO)
mcp = MCP.MCP3008(spi, cs)

chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
chan2 = AnalogIn(mcp, MCP.P2)
chan3 = AnalogIn(mcp, MCP.P3)
chan4 = AnalogIn(mcp, MCP.P4)
chan5 = AnalogIn(mcp, MCP.P5)
chan6 = AnalogIn(mcp, MCP.P6)
chan7 = AnalogIn(mcp, MCP.P7)

def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()

write("--- MCP3008 Raw Values ---")

try:
    while True:
        time.sleep(0.01)
        
        output = """
Chan0: {c0}
Chan1: {c1}
Chan2: {c2}
Chan3: {c3}
Chan4: {c4}
Chan5: {c5}
Chan6: {c6}
Chan7: {c7}
""".format(
            c0=chan0.value,
            c1=chan1.value,
            c2=chan2.value,
            c3=chan3.value,
            c4=chan4.value,
            c5=chan5.value,
            c6=chan6.value,
            c7=chan7.value
        )

        output = output.replace("\n", "\n\033[K")
        write(output)
        lines = len(output.split("\n"))
        write("\033[{}A".format(lines - 1))

        time.sleep(.1)

except KeyboardInterrupt:
    pass
