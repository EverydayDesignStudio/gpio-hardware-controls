#!/usr/bin/env python3

import RPi.GPIO as GPIO
import getch
import time
import sys

bcm_pins_left = [2, 3, 4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26]
bcm_pins_right = [14, 15, 18, 23, 24, 25, 8, 7, 1, 12, 16, 20, 21]
# bcm_pins_all = [2, 3, 4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 1, 12, 16, 20, 21]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUTTON = 2
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()


def get_next_pin(c: int):
    global BUTTON
    if c < len(bcm_pins_left):
        write('Left: BCM {n} is active'.format(n=bcm_pins_left[c]))
        BUTTON = bcm_pins_left[c]
        c = c + 1
    elif c < len(bcm_pins_left) + len(bcm_pins_right):
        write('Right: BCM {n} is active'.format(n=bcm_pins_right[c - 15]))
        BUTTON = bcm_pins_right[c - 15]
        c = c + 1
    else:  # switch back to the left side
        c = 0

    return c


def main():
    write("---Iterates through every GPIO pin to ensure proper connections---\n")
    SPEED = 6  # time per pin in seconds
    counter = 0
    timer = time.time()

    while True:
        if time.time() - timer > SPEED:
            timer = time.time()
            counter = get_next_pin(counter)
            # write("BCM {n} is now active".format(n=BUTTON))
            GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Button detection
        input1 = GPIO.input(BUTTON)
        if input1==False:
            output = '\nButton is pressed'
        else:
            output = '\nButton is not pressed'
        time.sleep(0.05)

        output = output.replace("\n", "\n\033[K")
        write(output)
        lines = len(output.split("\n"))
        write("\033[{}A".format(lines - 1))

if __name__ == "__main__":
    main()
