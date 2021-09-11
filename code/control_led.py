import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,0)
time.sleep(3)
GPOI.output(12,1)
GPIO.cleanup()

# for running this file sudo python control_led.py