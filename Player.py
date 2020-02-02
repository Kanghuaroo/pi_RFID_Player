#!/usr/bin/env python

#import sys
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import spotipy
import spotipy.util as util
from PlaybackModifier import PlaybackModifier
from Reader import Reader

#init of pin stuff
#check GPIO pin mode
if GPIO.getmode() == 10:
    #GPIO.BOARD
    button1 = 40
    button2 = 38
    button3 = 32
elif GPIO.getmode() == 11:
    #GPIO.BCM
    button1 = 21
    button2 = 20
    button3 = 12
else:
    GPIO.setmode(GPIO.BOARD)
    button1 = 40
    button2 = 38
    button3 = 32
Pins = [button1, button2, button3]
rfid = SimpleMFRC522()
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
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


try:
    reader.update_LCD()
    
    while True:
        print("Scan a Card")
        text = rfid.read()
        #wait a sec to see if more are pressed
        if GPIO.input(button1) == GPIO.HIGH or GPIO.input(button2) == GPIO.HIGH or GPIO.input(button3) == GPIO.HIGH:
            print("Wait...")
            reader.write_to_LCD("Please Wait...")
            print(button1, button2, button3)
            print(GPIO.input(button1),
                    GPIO.input(button2),
                    GPIO.input(button3))
            sleep(1)

        if (GPIO.input(button1) == GPIO.HIGH and GPIO.input(button2) == GPIO.HIGH) or (GPIO.input(button2) == GPIO.HIGH and GPIO.input(button3) == GPIO.HIGH):
            print("Stop Holding")
            reader.write_to_LCD("Stop Holding")
            sleep(1)
            reader.write_to_card(rfid, Pins)
        
        elif GPIO.input(button1) == GPIO.HIGH:
            print('skip')
            playback.skip()
        elif GPIO.input(button2) == GPIO.HIGH:
            print('pasue')
            playback.pause()
        elif GPIO.input(button3) == GPIO.HIGH:
            print('rewind time')
            playback.rewind()
        else:
            playback.changeSong(text)

        sleep(2)
        reader.update_LCD()
        sleep(3)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
