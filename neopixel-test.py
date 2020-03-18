#!/usr/bin/env python3

import board
import neopixel
import time

def main():
    PIN = int(input('Input pin of Neo Pixel: '))
    LENGTH = int(input('How long is your strip of Neo Pixels? '))

    if PIN == 18:
        print('Pin 18')
        PIN = board.D18
    elif PIN == 12:
        print('Pin 12')
        PIN = board.D12
    elif PIN == 21:
        print('Pin 21')
        PIN = board.D21
    else:
        raise Exception('Pin was [{p}]  |  Neo Pixels require 12, 18, or 21.'.format(p=PIN))

    pixels = neopixel.NeoPixel(PIN, LENGTH)  # Raspberry Pi wiring!

    # Light up the first NeoPixel red
    pixels[0] = (255, 0, 0)
    time.sleep(5)
    pixels[0] = (0, 0, 0)
    # Light up the last NeoPixel blue
    pixels[LENGTH-1] = (0, 0, 255)
    time.sleep(5)
    # Light up all the NeoPixels to a light white
    pixels.fill((100, 100, 100))
    time.sleep(15)
    # Turn off the NeoPixels
    pixels.fill((0, 0, 0))


if __name__ == "__main__":
    main()
