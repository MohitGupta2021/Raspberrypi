
'''we can also used
rgb=[11,13,15]
for pin in rgb:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,1)

'''

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.output(11,1)
GPIO.output(13,1)
GPIO.output(15,1)
try:
    while(True):
        request=raw_input("rgb which press 1 for on and 0 for f")
        if(len(request) ==3):
            GPIO.output(11,int(request[0]))
            GPIO.output(13,int(request[1]))
            GPIO.output(15,int(request[2]))
except KeyboardInterrupt:

    GPIO.cleanup()


