from RPLCD.gpio import CharLCD
from RPi import GPIO
from time import sleep


class LCD_Screen:

    def __init__(self):
        lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, 
                pins_data=[33,31,29,36],numbering_mode=GPIO.BOARD)
    
    #Basic write to LCD Screen
    def write(self, Str):
        self.lcd.write_string(Str)
        sleep(5)
        self.lcd.clear()

    #Print a song to the LCD Screen
    def writeSong(self, song, time):
        self.lcd.clear()
        if len(song) > 16:
            song = song[:16]
        self.lcd.write_string(song)
        self.lcd.write_string(time)
