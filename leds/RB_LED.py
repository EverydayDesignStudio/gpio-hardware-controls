#!/usr/bin/env python3
# ------------------------------------------------------------------------------
#  Script for testing a RED and BLUE LED
# ------------------------------------------------------------------------------

# Import system modules
import RPi.GPIO as gpio      # For interfacing with the pins of the Raspberry Pi
import time                  # For unix timestamps

# Pin Configurations
print('On Capra the RED was 13')
LED_RED = int(input('Input RED LED BCM pin: '))
print('On Capra the BLUE was 26')
LED_BLUE = int(input('Input BLUE LED BCM pin: '))

# LED_BLUE = 26           # BOARD - 37
# LED_RED = 13            # BOARD - 33

gpio.setwarnings(False)             # Turn off GPIO warnings
gpio.setmode(gpio.BCM)              # Broadcom pin numbers
gpio.setup(LED_BLUE, gpio.OUT)      # Blue LED led1
gpio.setup(LED_RED, gpio.OUT)       # Red LED led2


# Functions
# ------------------------------------------------------------------------------
def turn_off():
    gpio.output(LED_BLUE, False)
    gpio.output(LED_RED, False)


def turn_blue():
    gpio.output(LED_BLUE, True)


def turn_red():
    gpio.output(LED_RED, True)


def turn_purple():
    gpio.output(LED_BLUE, True)
    gpio.output(LED_RED, True)


# Helper function for blinking
def blink(pin: int, repeat: int, interval: float) -> None:
    for i in range(repeat):
        gpio.output(pin, True)
        time.sleep(interval)
        gpio.output(pin, False)
        time.sleep(interval)


def blink_red_blue():
    blink(LED_RED, 4, 0.3)
    blink(LED_BLUE, 4, 0.3)


def blink_red_quick():
    blink(LED_RED, 10, 0.1)


# Main Loop
# ------------------------------------------------------------------------------
def main():
    print("🚨 Starting LED Testing 🚨")
    turn_off()
    blink_red_quick()
    time.sleep(2)

    turn_blue()
    time.sleep(3)
    turn_off()
    time.sleep(1)
    turn_red()
    time.sleep(3)
    turn_off()
    turn_purple()
    time.sleep(3)
    turn_off()

    # blink(LED_RED, 1, 0.3)
    # time.sleep(1)
    # blink(LED_RED, 4, 0.2)
    # time.sleep(1)
    # blink(LED_RED, 2, 0.2)
    # time.sleep(1)
    # blink(LED_RED, 1, 0.3)
    # time.sleep(1)
    # blink(LED_BLUE, 1, 0.1)
    # time.sleep(1)
    # blink_after_crash()
    # time.sleep(2)

    print("🚨 FINISHED 🚨")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print('===== Error ===== ')
        print(error)
