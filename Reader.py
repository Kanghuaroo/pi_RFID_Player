import spotipy
import spotipy.util as util
import RPi.GPIO as GPIO
from LCD_Screen import LCD_Screen
from PlayerWriter import PlayerWriter

class Reader:

    def __init__(self, sp):
        self.lcd = LCD_Screen()
        self.readerPlayer = sp

    def update_LCD(self):
        self.lcd.write(self.readerPlayer.current_playback()['item']['name'])
    
    def write_to_LCD(self, String):
        self.lcd.write(String)
    def write_to_card(self, rfid, button):
        self.lcd.write("What to write?\n 1Trk 2Art 3Albm")
        

        answer = False
        while not answer:
            #track
            if GPIO.input(button[2]) == GPIO.HIGH:
                uri = self.readerPlayer.current_playback()['item']['uri']
                PlayerWriter(uri, rfid)
                answer = True
            #artist
            elif GPIO.input(button[1]) == GPIO.HIGH:
                uri = self.readerPlayer.current_playback()['item']['artists'][0]['uri']
                PlayerWriter(uri, rfid)
                answer = True
            #album/playlists
            elif GPIO.input(button[0]) == GPIO.HIGH:
                self.lcd.countdown("Choose - \n 1.) Album 2.) Playlist", 10, '\n')
                if GPIO.input(button[2]) == GPIO.HIGH:
                    self.lcd.write("Album Chosen")
                    uri = self.readerPlayer.current_playback()['item']['album']['uri']
                elif GPIO.input(button[1]) == GPIO.HIGH:
                    self.lcd.write("Playlist Chosen")
                    uri = self.readerPlayer.current_playback()['context']['uri']
                else:
                    self.lcd.write("Album Chosen \n by default")
                    uri = self.readerPlayer.current_playback()['item']['album']['uri']
    
                PlayerWriter(uri, rfid)
                answer = True
        self.lcd.write("Write \nComplete")


