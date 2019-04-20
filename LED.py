import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(24, gpio.OUT)

x = 1
h = 100
while x < h:
    if x % 2 == 0:
        gpio.output(24, True)
        time.sleep(.2)
        x += 1
    else:
        gpio.output(24, False)
        time.sleep(.2) 
        x += 1
