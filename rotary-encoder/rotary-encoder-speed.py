#!/usr/bin/env python3

from RPi import GPIO
from datetime import datetime
from time import sleep
import queue
from input_correct_data import *

clk = input_int('Input pin of clockwise: ')
cnt = input_int('Input pin of counterclockwise: ')
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(cnt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

PERIOD = 500
counter = 0
clkLastState = GPIO.input(clk)
last_time = datetime.now().timestamp()
# q = queue.Queue(10)
l = list()


def calculate_speed():
    global last_time
    difference = round(datetime.now().timestamp() - last_time, 5)
    # data sanitation: clean up random stray values that are extremely low
    if difference < .001:
        difference = .1

    if len(l) > 10:
        l.pop()
    l.insert(0, difference)
    average = sum(l)/len(l)

    last_time = datetime.now().timestamp()

    # print(difference)
    # print('The average time between clicks is: {t}'.format(t=average))

    #   .3   .07   .02
    if average >= .3:
        print('slow')
    elif average >= .07 and average < .3:
        print('medium')
    elif average >= .02 and average < .07:
        print('fast')
    else:
        print('super-duper fast')

while True:
    clkState = GPIO.input(clk)
    cntState = GPIO.input(cnt)
    if clkState != clkLastState:
        if cntState != clkState:
            counter += 1
            calculate_speed()
        else:
            counter -= 1
            calculate_speed()
        print('this is the current counter: {c}\n'.format(c=counter))
    clkLastState = clkState
