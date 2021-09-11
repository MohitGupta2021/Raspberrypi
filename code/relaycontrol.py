#relay models
''' for relay control optocoupler(optoisolator), DIODe'''
''' model:srd-05VDC-SL-C\
input volatge-5v dc\
input current -60 mA\
output ratings(TUV):
10A-250 VAC
10A-30VDC

output ratings(UL):
10A-125 VAC
10A-28VDC
****mains electricity can kill***
24 pin as GPIO board connnect to the relay
and output of realay connect to dc motor
'''

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(24,GPIO.OUT,intial=0)
try:
    while True:
        GPIO.output(24,1)
        time.sleep(3)
        GPIO.output(24,0)
        time.sleep(3)

except KeyboardInterrupt:
    pass
GPIO.cleanup()



