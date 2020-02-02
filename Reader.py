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

    def write_to_card(self, rfid, button):
        self.lcd.write("What to write?\n 1Trk 2Albm 3Art")
        

        answer = False
        while not answer:
            if GPIO.input(button[0]) == GPIO.HIGH:
                PlayerWriter(self.readerPlayer.current_playback(), rfid)
                answer = True

            elif GPIO.input(button[1]) == GPIO.HIGH:
                PlayerWriter(self.readerPlayer.current_playback(), rfid)
                answer = True

            elif GPIO.input(button[2]) == GPIO.HIGH:
                PlayerWriter(self.readerPlayer.current_playback(), rfid)
                answer = True


