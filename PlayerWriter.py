#!/usr/bin/env python

import spotipy
import spotipy.util as util
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def PlayerWriter(uri, rfid):
    print('Card to Write ')
    msg = uri
    text = msg['item']['uri']
    print(msg['item']['uri'])
    
    print('writing ' + text)
    print("Now place your tag to write")
    rfid.write(text)
    print("Written")

