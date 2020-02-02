#!/usr/bin/env python

import sys
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from PlaybackModifier import PlaybackModifier
from Reader import Reader

rfid = SimpleMFRC522()
#lcd = LCD_Screen()

playback = PlaybackModifier()
reader = Reader()

try:
    while True:
        playback.changeSong(rfid)
        reader.update_LCD()

        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
