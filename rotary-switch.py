#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()
     
write("--- Rotary Switch Values ---")

while True:
    input13 = GPIO.input(13)
    input19 = GPIO.input(19)
    input26 = GPIO.input(26)
    output = '\n13: {}, \n19: {}, \n26: {}'.format(input13, input19, input26)
    time.sleep(0.05)

    output = output.replace("\n", "\n\033[K")
    write(output)
    lines = len(output.split("\n"))
    write("\033[{}A".format(lines - 1))
