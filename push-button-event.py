#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import sys

BUTTON = int(input('Input button pin: '))
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count_press = 0
count_release = 0


def button_pressed(self):
    global count_press
    count_press += 1
    print("Button Pressed {c}xs".format(c=count_press))


def button_released(self):
    global count_release
    count_release += 1
    print("Button Released {c}xs".format(c=count_release))


def main():
    # NOTE: no rebouncing
    # GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=button_handler)

    # NOTE: detection on Falling / Pressing
    # GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=button_pressed, bouncetime=200)

    # NOTE: detection on Rising / Release
    GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=button_released, bouncetime=200)

    while True:
        continue


if __name__ == "__main__":
    main()
