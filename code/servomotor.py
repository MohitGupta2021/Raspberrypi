'''model=towerprosg90
voltage-4-8v dc
speed 60 deg in 0.1 s
torquue -1-6 kg cm
weight 9g
pulse width-0.5ms-2.5ms
for 0* -0.5 ms
for neutral -1.5 ms
for 180* -2.5 ms
F=50hz/dc
t=20 ms



'''
'''for pwm you can use this code'''
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)#11 pin number and 50HZ
pwm.start(7.5)
try:
    while True:

            pwm.ChangeDutyCycle(7.5)#neutral
            sleep(1)
            pwm.ChangeDutyCycle(12.5)#180 degree
            sleep(1)
            pwm.ChangeDutyCycle(2.5)#0 degree
            sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
