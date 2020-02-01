#!/usr/bin/env python3

import PRi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

scanner = SimpleMFRC522()

try:
	text, msg = input reader.read()
	print(text)
	print(msg)
finally:
	GPIO.cleanup()
