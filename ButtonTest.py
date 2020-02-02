import RPi.GPIO as GPIO
from time import sleep

#GPIO.setwarnings(False)
#physical pin #'s
GPIO.setmode(GPIO.BCM)
button1 = 40
button2 = 38
button3 = 32
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while False:
    if GPIO.input(button1) == GPIO.HIGH:
        print("Button 1 Pressed!")
    elif GPIO.input(button2) == GPIO.HIGH:
        print("Button 2 Pressed!!")
    elif GPIO.input(button3) == GPIO.HIGH:
        print("Button 3 Pressed!!!")
    else:
        print("Not Pressed")
mode = GPIO.getmode()
print(mode, GPIO.getmode())
while True:
    try:
            print(button1, button2, button3)
            print(GPIO.input(button1) == GPIO.HIGH,
                    GPIO.input(button2) == GPIO.HIGH,
                    GPIO.input(button3) == GPIO.HIGH)
            sleep(1)
    except KeyboardInterrupt:
        print(GPIO.getmode())
        GPIO.cleanup()
        print(GPIO.getmode())
        break

