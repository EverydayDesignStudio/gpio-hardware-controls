#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import sys

BUTTON = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()
     
write("--- Push Button Values ---")

while True:
    input13 = GPIO.input(BUTTON)
    if input13 == False:
        output = '\nButton is pressed'
    else:
        output = '\nButton is not pressed'
    time.sleep(0.05)

    output = output.replace("\n", "\n\033[K")
    write(output)
    lines = len(output.split("\n"))
    write("\033[{}A".format(lines - 1))