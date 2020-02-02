#!/usr/bin/env python

import spotipy
import spotipy.util as util
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from CurrentSongInfo import currentPlayback

scope = 'user-read-playback-state'
ID='bf8057981097462a95729337360b7f03'
SECRET='264737bc4ad443429635d93babefc597'
URI='https://localhost/'

token = util.prompt_for_user_token(username='lyirk',scope=scope,client_id=ID,client_secret=SECRET, redirect_uri=URI)
sp = spotipy.Spotify(auth=token)
reader = SimpleMFRC522()

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

