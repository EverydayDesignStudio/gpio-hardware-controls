#!/usr/bin/env python3

import RPi.GPIO as gpio
import time

LED = int(input('Input pin of LED: '))

gpio.setwarnings(False)     # Turn off GPIO warning
gpio.setmode(gpio.BCM)
gpio.setup(LED, gpio.OUT)

gpio.output(LED, True)
