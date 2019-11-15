#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from piezo_player import PiezoPlayer


def main():
    PIN = int(input('Input piezo pin: '))
    GPIO.setmode(GPIO.BCM)
    # GPIO.setwarnings(False)

    piezo = PiezoPlayer(pin=PIN)

    piezo.play_power_on_jingle()
    time.sleep(2)
    piezo.play_start_recording_jingle()
    time.sleep(2)
    piezo.play_still_recording_jingle()
    time.sleep(2)
    piezo.play_stop_recording_jingle()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:   # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print('\n THE PROGRAM STOPPED.')
