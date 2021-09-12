import RPi.GPIO as GPIO
import time
button=7
led=12
GPIO.setmode(GPIO.BCM)
GPIO.setup(button,GPIO.IN,GPIO.PUD_UP)
try:
    while True:
        if(GPIO.input(button==0)):
            GPIO.output(led,GPIO.HIGH)
            time.sleep(0.5)
        else:
            GPIO.output(led,GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()


