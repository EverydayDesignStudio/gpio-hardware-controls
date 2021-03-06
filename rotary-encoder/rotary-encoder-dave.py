#!/usr/bin/env python3

from RPi import GPIO
from time import sleep

clk = int(input('Input pin of clockwise: '))
cnt = int(input('Input pin of counterclockwise: '))

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(cnt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

while True:
    clkState = GPIO.input(clk)
    cntState = GPIO.input(cnt)
    if clkState != clkLastState:
        if cntState != clkState:
            counter += 1
        else:
            counter -= 1
        print(counter)
    clkLastState = clkState
    sleep(0.05)
