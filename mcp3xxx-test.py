import time
import busio
import digitalio
import board

import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# import mcp3008 as MCP
# from analog_in import AnalogIn

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)

chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
diff0 = AnalogIn(mcp, MCP.P0, MCP.P1)
chan6 = AnalogIn(mcp, MCP.P6)
diff6 = AnalogIn(mcp, MCP.P6, MCP.P7)
chan7 = AnalogIn(mcp, MCP.P7)
diff7 = AnalogIn(mcp, MCP.P6, MCP.P6)

while True:
    v0 = chan0.value >> 6
    v1 = chan1.value >> 6
    d0 = diff0.value >> 6
    v6 = chan6.value >> 6
    d6 = diff6.value >> 6
#    print("7 :", type(chan6.value))
#    print("6 :", type(chan7.value))
#    print("diff0: ", type(diff0))
#    print("diff0.value: ", type(diff0.value))
#    print("diff7: ", type(diff7))
#    print("diff7.value: ", type(diff7.value))
    v7 = chan7.value >> 6
#    print(type(diff7.value))
    d7 = diff7.value >> 6

#    print('Raw ADC Value: {}, {}'.format(chan0.value, chan1.value))
#    print('Differential: {}'.format(diff0.value))

#    print('@@ Raw ADC Value: {}, {}'.format(v0, v1))
#    print('   Differential: {}'.format(d0))
#    print('@@  Channel 6: {}, diff: {}'.format(v6, d6))
    print('    Diff6: {}, Diff7: {}'.format(d6, d7))

#    print('ADC Voltage: ' + str(channel.voltage) + 'V')
    time.sleep(0.5)
