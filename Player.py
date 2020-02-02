#!/usr/bin/env python

import sys
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import spotipy
import spotipy.util as util
from PlaybackModifier import PlaybackModifier
from Reader import Reader

ID='bf8057981097462a95729337360b7f03'
SECRET='264737bc4ad443429635d93babefc597'
URI='https://localhost/'

scope = 'user-read-playback-state user-modify-playback-state'
token = util.prompt_for_user_token(username='lyirk',
        scope=scope,client_id=ID,client_secret=SECRET, redirect_uri=URI)

#init of player and classes
sp = spotipy.Spotify(auth=token)
reader = Reader(sp)
playback = PlaybackModifier(sp)

#init of pin stuff
button1 = 40
button2 = 38
button3 = 32
rfid = SimpleMFRC522()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        playback.changeSong(rfid)
        reader.update_LCD()
        
        if GPIO.input(button1) == GPIO.HIGH:
            print("Button 1 Pressed!")
            playback.skip()
        elif GPIO.input(button2) == GPIO.HIGH:
            print("Button 2 Pressed!!")
            playback.pause()
        elif GPIO.input(button3) == GPIO.HIGH:
            print("Button 3 Pressed!!!")

        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
