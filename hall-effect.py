#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import sys
from input_correct_data import *

HALL_PIN = input_int('Input pin of sensor: ')
GPIO.setmode(GPIO.BCM)
GPIO.setup(HALL_PIN, GPIO.IN)
# GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()

write("--- Hall Effect Sensor ---")

while True:
    input_hall = GPIO.input(HALL_PIN)
    if input_hall is False:
        output = '\nMagnet near'
    else:
        output = '\nMagnet far'
    time.sleep(0.05)

    output = output.replace("\n", "\n\033[K")
    write(output)
    lines = len(output.split("\n"))
    write("\033[{}A".format(lines - 1))
