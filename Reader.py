#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
print('Scan')
try:
        text, msg = reader.read()
        print('text', text)
        print('msg', msg)
finally:
        GPIO.cleanup()
