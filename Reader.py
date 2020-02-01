#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
print('here')

try:
        text, msg = reader.read()
        print(text)
        print(msg)
        print('done')
finally:
        GPIO.cleanup()
        print('clean')
