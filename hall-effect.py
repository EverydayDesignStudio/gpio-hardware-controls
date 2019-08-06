#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import sys

HALL_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(HALL_PIN, GPIO.IN)
#GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()
     
write("--- Hall Effect Sensor ---")

while True:
    input_hall = GPIO.input(HALL_PIN)
    if input_hall == False:
        output = '\nMagnet near'
    else:
        output = '\nMagnet far'
    time.sleep(0.05)

    output = output.replace("\n", "\n\033[K")
    write(output)
    lines = len(output.split("\n"))
    write("\033[{}A".format(lines - 1))
