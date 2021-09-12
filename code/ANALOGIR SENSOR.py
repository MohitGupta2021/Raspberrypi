''' SENSOR AT AO and led at 4'''
import RPi.GPIO as GPIO
import time
import spidev
current_sensor=0
led=4
spi=spidev.SpiDev()
spi.open()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,0)
def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4,0]) #xfer2(list of values[, speed_hz, delay_usec, bits_per_word])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out
while True:
    value=analog_read(current_sensor)
    print("current_sensor:"+str(value)))
    if(value>200):
        GPIO.output(led,1)
    else:
        GPIO.output(led,0)
    sleep(0.5)

