import spotipy
import spotipy.util as util
from LCD_Screen import LCD_Screen
from PlayerWriter import PlayerWriter

class Reader:

    def __init__(self, sp):
        self.lcd = LCD_Screen()
        self.readerPlayer = sp

    def update_LCD(self):
        self.lcd.writeSong(self.readerPlayer.current_playback()['item']['name'])

    def write_to_card(self, uri):
        self.PlayerWriter(self.readerPlayer.currnet_playback()['item']['uri'])
