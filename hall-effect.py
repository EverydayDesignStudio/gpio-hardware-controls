#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import sys
from input_correct_data import *

HALL_PIN = input_int('Input pin of sensor: ')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(HALL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()


def full_write(output):
    output = output.replace("\n", "\n\033[K")
    write(output)
    lines = len(output.split("\n"))
    write("\033[{}A".format(lines - 1))


write("----- Test Hall Effect Sensor -----")


def main():
    while True:
        hall_effect_stat = ""

        if GPIO.input(HALL_PIN) == 0:
            hall_effect_stat = 'Magnet Near'

        output = """
Hall Effect:{he}
""".format(he=hall_effect_stat)
        full_write(output)

        time.sleep(0.1)


if __name__ == "__main__":
    main()
