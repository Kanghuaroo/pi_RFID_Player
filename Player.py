#!/usr/bin/env python

import sys
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import spotipy
import spotipy.util as util

scope = 'user-modify-playback-state'
ID='52f5fff3d7aa44d6a75522471ef094d7'
SECRET='15a676a209884a2bbaf28f1afc629e58'
URI='http://localhost/'

token = util.prompt_for_user_token(username='lyirk',scope=scope,client_id=ID,client_secret=SECRET, redirect_uri=URI)
sp = spotipy.Spotify(auth=token)
reader = SimpleMFRC522()

try:
    while True:
        print('Hold a Song Card Near...')
        #Song URI is in the text var
        id, text = reader.read()
        print("ID:  %s\nText: %s" % (id,text))
        text.strip()

        #what is text?
        if text.find('text') != 1:
            sp.start_playback(uris=text)
        elif text.find('playlist') != -1:
            sp.shuffle(state=True)
            sp.start_playback(context_uri=text)
        elif text.find('artist') != -1:
            sp.shuffle(state=True)
            sp.start_playback(context_uri=text)

        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
