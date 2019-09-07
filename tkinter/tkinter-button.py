#!/usr/bin/env python3

# Imports
from PIL import ImageTk, Image          # Pillow image functions
from tkinter import Tk, Canvas, Label   # Tkinter, GUI framework in use
import time
import datetime

from gpiozero import Button         # Rotary encoder, detected as button
from RPi import GPIO                # GPIO pin detection for Raspberry Pi
from time import sleep

# Setup GPIO
play_pause_button = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(play_pause_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Slideshow class which is the main class that runs and is listening for events
class Slideshow:
    def __init__(self, win):
        # Setup the window
        self.window = win
        self.window.title("Capra Slideshow")
        self.window.geometry("250x250")
        self.window.configure(background='black')
        self.canvas = Canvas(root, width=720, height=1280, background="#5caaff", highlightthickness=0)
        self.canvas.pack(expand='yes', fill='both')

        # Bind to events in which to listen
        self.window.bind('<Left>', self.leftKey)
        self.window.bind('<Right>', self.rightKey)
        self.window.bind('<space>', self.space_key)

        self.window.bind(GPIO.add_event_detect(play_pause_button, GPIO.FALLING, callback=self.button_pressed))
        # self.rotary_button_pressed = GPIO.input(rotary_button)  # not sure if this is correct
        
        self.count = 0
        
    # KEYBOARD KEYS
    def rightKey(self, event):
        print('increment the count')

    def leftKey(self, event):
        print("decrement the count")

    def space_key(self, event):
        print('space key pressed')

    def button_pressed(self, event):
        self.count = self.count + 1
        print('Count: {c}'.format(c=self.count))
        time.sleep(0.4)


# Create the root window
root = Tk()
root.bind("<Escape>", exit)
slide_show = Slideshow(root)
root.mainloop()
