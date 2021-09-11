import RPi.GPIO as GPIO
import time
led_pin=11
button_pin=36
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin,GPIO.OUT)
    GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
def loop():
    while True:
        if GPIO.input(button_pin)==0:
            GPIO.output(button_pin,1)
        else:
            GPIO.output(button_pin,0)
def destroy():
    GPIO.output(led_pin,0)
    GPIO.cleanup()
if __name__=='__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()