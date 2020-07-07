#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import sys

BUTTON = int(input('Input button pin: '))
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)


print("--- Wait for Edge ---\n")


def main():
    while True:
        print("loop is waiting for you to RELEASE the button...")
        GPIO.wait_for_edge(BUTTON, GPIO.RISING)
        print("Nice! You've RELEASED the button\n")

        print("loop is waiting for you to PRESS the button...")
        GPIO.wait_for_edge(BUTTON, GPIO.FALLING)
        print("Nice! You've PRESSED the button\n")


if __name__ == "__main__":
    main()
