#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import sys
from input_correct_data import *

pos1 = input_int('Input pin 1: ')
pos2 = input_int('Input pin 2: ')
pos3 = input_int('Input pin 3: ')

GPIO.setmode(GPIO.BCM)
GPIO.setup(pos1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pos2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pos3, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()

write("--- Rotary Switch Values ---")

while True:
    input1 = GPIO.input(pos1)
    input2 = GPIO.input(pos2)
    input3 = GPIO.input(pos3)
    output = '\n{}: {}, \n{}: {}, \n{}: {}'.format(pos1, input1, pos2, input2, pos3, input3)
    time.sleep(0.05)

    output = output.replace("\n", "\n\033[K")
    write(output)
    lines = len(output.split("\n"))
    write("\033[{}A".format(lines - 1))
