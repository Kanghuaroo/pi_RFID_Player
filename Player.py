#!/usr/bin/env python

import sys
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from PlaybackModifier import PlaybackModifier
from Reader import Reader

reader = SimpleMFRC522()
#lcd = LCD_Screen()

playback = PlaybackModifier()
reader = Reader() 

try:
    while True:
        playback.changeSong()
        reader.update_LCD()

        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
