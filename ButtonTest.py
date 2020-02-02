import RPi.GPIO as GPIO

#GPIO.setwarnings(False)
#physical pin #'s
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(40) == GPIO.HIGH:
        print("Button 1 Pressed!")
    elif GPIO.input(38) == GPIO.HIGH:
        print("Button 2 Pressed!!")
    elif GPIO.input(32) == GPIO.HIGH:
        print("Button 3 Pressed!!!")
    else:
        print("Not Pressed")
