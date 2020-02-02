#!/usr/bin/env python

import spotipy
import spotipy.util as util
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def PlayerWriter(sp):
    print('Card to Write ')
    msg = (sp.current_playback())
    
    text = msg['item']['uri']
    
    print(msg['item']['uri'])
    
    try:
        print('writing ' + text)
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
    finally:
        GPIO.cleanup()

