#!/usr/bin/env python3

from RPi import GPIO
from time import sleep

clk = int(input('Input pin of clockwise: '))
cnt = int(input('Input pin of counterclockwise: '))

encoder = KY040(clk, cnt)
encoder.start()

while True:
    encoder

# import RPi.GPIO as GPIO
# import time import sleep


class KY040:
    ROTARY_DEBOUNCE = 2
    SWITCH_DEBOUNCE = 200
    BREAK_COUNTER = 199999

    def __init__(self, clockPin, dataPin, switchPin, rotaryCallback, switchCallback):
        # persist values
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.switchPin = switchPin
        self.rotaryCallback = rotaryCallback
        self.switchCallback = switchCallback

        # setup pins
        GPIO.setup(clockPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(dataPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def start(self):
        GPIO.add_event_detect(self.clockPin, GPIO.FALLING, callback=self._clockCallback, bouncetime=self.ROTARY_DEBOUNCE)
        GPIO.add_event_detect(self.dataPin, GPIO.FALLING, callback=self._dataCallback, bouncetime=self.ROTARY_DEBOUNCE)
        GPIO.add_event_detect(self.switchPin, GPIO.FALLING, callback=self._switchCallback, bouncetime=self.SWITCH_DEBOUNCE)

    def stop(self):
        GPIO.remove_event_detect(self.clockPin)
        GPIO.remove_event_detect(self.dataPin)
        GPIO.remove_event_detect(self.switchPin)

    def _clockCallback(self, pin):
        Switch_A = GPIO.input(self.clockPin)
        Switch_B = GPIO.input(self.dataPin)

        if (Switch_A == 0) and (Switch_B == 1):
            if(not self.waitForRotaryState(0, 0)):
                return
            if(not self.waitForRotaryState(1, 1)):
                return
            self.rotaryCallback(1)

    def _dataCallback(self, pin):
        Switch_A = GPIO.input(self.clockPin)
        Switch_B = GPIO.input(self.dataPin)
        breakCounter = self.BREAK_COUNTER

        if (Switch_A == 1) and (Switch_B == 0):
            if(not self.waitForRotaryState(0, 0)):
                return
            if(not self.waitForRotaryState(1, 1)):
                return
            self.rotaryCallback(0)

    def waitForRotaryState(self, switch_A, switch_B):
        Switch_A = GPIO.input(self.clockPin)
        Switch_B = GPIO.input(self.dataPin)
        breakCounter = self.BREAK_COUNTER

        while Switch_A == (not switch_A) or Switch_B == (not switch_B):
            Switch_A = GPIO.input(self.clockPin)
            Switch_B = GPIO.input(self.dataPin)
            breakCounter = breakCounter - 1
            if(breakCounter <= 0):
                return False
        return True

    def _switchCallback(self, pin):
        self.switchCallback()
