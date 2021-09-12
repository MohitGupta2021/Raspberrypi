import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
leds_pin=[4,17,22,10,9,11]
for l in range(6):
    GPIO.setup(leds_pin[l],GPIO.OUT)
    GPIO.output(leds_pin[l],0)
random.seed()
try:
    while True:
        for l in range(6):
            GPIO.output(leds_pin[l],False)
        result=random.randint(0,5)
        print "led NO ="+str(result)
        GPIO.output(leds_pin[result],GPIO.HIGH)
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    