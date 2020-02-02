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

sp = spotipy.Spotify(auth=token)

reader = Reader(sp)
playback = PlaybackModifier(sp)

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
