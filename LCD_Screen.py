from RPLCD import CharLCD
from time import sleep

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33,31,29,36])

lcd.write_string(u"Hello World!")

sleep(5)

lcd.clear()
