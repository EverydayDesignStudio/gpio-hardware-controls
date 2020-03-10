#!/usr/bin/env python3

import rotaryio
import board

encoder = rotaryio.IncrementalEncoder(board.D23, board.D24)
last_position = None
while True:
    position = encoder.position
    if last_position is None or position != last_position:
        print(position)
    last_position = position

# import pulseio
# import time
# from board import *

# pwm = pulseio.PWMOut(D13)
# pwm.duty_cycle = 2 ** 15
# time.sleep(0.1)
