import RPi.GPIO as gpio
import time
from input_correct_data import *

LED = input_int('Input pin of LED: ')
gpio.setmode(gpio.BCM)
gpio.setup(LED, gpio.OUT)

x = 1
h = 100
while x < h:
    if x % 2 == 0:
        gpio.output(LED, True)
        time.sleep(.2)
        x += 1
    else:
        gpio.output(LED, False)
        time.sleep(.2) 
        x += 1
