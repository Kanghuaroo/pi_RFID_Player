#!/usr/bin/env python

import sys
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import spotipy
import spotipy.util as util
from LCD_Screen import LCD_Screen
from PlayerWriter import PlayerWriter

ID='bf8057981097462a95729337360b7f03'
SECRET='264737bc4ad443429635d93babefc597'
URI='https://localhost/'

scope = 'user-modify-playback-state'
modifyToken = util.prompt_for_user_token(username='lyirk',scope=scope,client_id=ID,client_secret=SECRET, redirect_uri=URI)

scope = 'user-read-playback-state'
songToken = util.prompt_for_user_token(username='lyirk',scope=scope,client_id=ID,client_secret=SECRET, redirect_uri=URI)

modifyPlayer = spotipy.Spotify(auth=modifyToken)
readerPlayer = spotipy.Spotify(auth=songToken)

reader = SimpleMFRC522()
lcd = LCD_Screen()


try:
    while True:
        print('Hold a Song Card Near...')
        #Song URI is in the text var
        text = reader.read()
        text = str(text[1])
        print("Text: " + (text))
        text = text.strip(' ')
        print(len(text))
        print(text + "end")

        #how to play text
        if text.find('text') != 1:
            modifyPlayer.start_playback(uris=[text])
        elif text.find('playlist') != -1:
            modifyPlayer.shuffle(state=True)
            modifyPlayer.start_playback(context_uri=text)
        elif text.find('artist') != -1:
            modifyPlayer.shuffle(state=True)
            modifyPlayer.start_playback(context_uri=text)
        
        #Print to LCD Screen
        #lcd.writeSong()

        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
