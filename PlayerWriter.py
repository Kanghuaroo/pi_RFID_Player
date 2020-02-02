#!/usr/bin/env python

import spotipy
import spotipy.util as util
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

scope = 'user-modify-playback-state'
ID='52f5fff3d7aa44d6a75522471ef094d7'
SECRET='15a676a209884a2bbaf28f1afc629e58'
URI='http://localhost/'

token = util.prompt_for_user_token(username='lyirk',scope=scope,client_id=ID,client_secret=SECRET, redirect_uri=URI)
sp = spotipy.Spotify(auth=token)
reader = SimpleMFRC522()

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

