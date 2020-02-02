import Adafruit_CharLCD as LCD
from time import sleep


class LCD_Screen:

    def __init__(self):
        #GPIO #, not pin#
        rs = 26 #37
        en = 19 #35
        d4 = 13 #33
        d5 = 6 #31
        d6 = 5 #29
        d7 = 16 #36
        backlight = 2
        cols = 16
        rows = 2
        self.lcd = LCD.Adafruit_CharLCD(rs,en,d4,d5,d6,d7,cols,rows,backlight)
    
    #Print Song name
    def writeSong(self, song):
        self.lcd.clear()
        if len(song) > 16:
            self.lcd.message(song[:16])
            self.lcd.message('\n' + song[16:])
        else:
            self.lcd.message(song)
