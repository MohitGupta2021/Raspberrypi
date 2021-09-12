'''2 pins 1connected to chaanl 0 AND OTHER CONNECT TO CHAANEL 1'''
import RPi.GPIO as GPIO
import time
import spidev

joyx=0
joyy=1
spi=spidev.SpiDev()
spi.open(0,0)
def readadc(channel):
    r=spi.xfer2([1,8+adcnum << 4,0])
    adcout=((r[1] &3) <<8)+r[2]
    return adcout
while True:
    x=readadc(joyx)
    y=readadc(joyy)
    print("X:" + str(x) + "Y: " +str(y))
    if(x>1000):
        print(reached to max value)
    sleep(0.2)