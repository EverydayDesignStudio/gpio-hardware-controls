#!/usr/bin/env python3

# ADXL345 Accelerometer from Adafruit

import adafruit_adxl34x
import board
import busio
import math
import sys
import time

i2c = busio.I2C(board.SCL, board.SDA)
adxl345 = adafruit_adxl34x.ADXL345(i2c)

# while True:
    # print("%f %f %f" % adxl345.acceleration)
    # print(adxl345.acceleration)
    # time.sleep(0.2)

# Tuple of x, y, z acceleration values
# lsm = LSM303D(0x1d)  # Change to 0x1e if you have soldered the address jumper


def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()


write("""------ ADXL345 Accelerometer from Adafruit ------
Tells which side of accelerometer is pointed up

""")


try:
    while True:
        # xyz = lsm.accelerometer()
        xyz = adxl345.acceleration

        ax = round(xyz[0], 7)
        ay = round(xyz[1], 7)
        az = round(xyz[2], 7)

        pitch = round(180 * math.atan(ax/math.sqrt(ay*ay + az*az))/math.pi, 3)
        roll = round(180 * math.atan(ay/math.sqrt(ax*ax + az*az))/math.pi, 3)
        yaw = round(180 * math.atan(az/math.sqrt(ax*ax + az*az))/math.pi, 3)
        # yaw = 180 * atan (accelerationZ/sqrt(accelerationX*accelerationX + accelerationZ*accelerationZ))/M_PI;

        if (pitch) > 45:
            orientation = 'X ↑'
        elif (pitch) < -45:
            orientation = 'x ↓'
        elif (roll) > 45:
            orientation = 'Y ↑'
        elif (roll) < -45:
            orientation = 'Y ↓'
        elif (abs(pitch) < 10 and abs(roll) < 10 and yaw >= 0):
            orientation = 'Z ↑ Flat on breadboard'
        elif (abs(pitch) < 10 and abs(roll) < 10 and yaw < 0):
            orientation = 'Z ↓'
        else:
            orientation = '??  Unsure exact orientation'

        output = """
Accelerometer: {x}g {y}g {z}g
Pitch: {p}
Roll: {r}
Yaw: {yw}

Orientation: {o}

""".format(
            x=ax,
            y=ay,
            z=az,
            p=pitch,
            r=roll,
            yw=yaw,
            o=orientation
        )

        output = output.replace("\n", "\n\033[K")
        write(output)
        lines = len(output.split("\n"))
        write("\033[{}A".format(lines - 1))

        time.sleep(.1)

except KeyboardInterrupt:
    pass
