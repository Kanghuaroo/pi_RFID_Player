#!/usr/bin/env python

import sys
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from PlaybackModifier import PlaybackModifier
from Reader import Reader

reader = Reader()
playback = PlaybackModifier()

rfid = SimpleMFRC522()


try:
    while True:
        playback.changeSong(rfid)
        reader.update_LCD()

        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
