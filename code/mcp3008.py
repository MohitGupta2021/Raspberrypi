'''
mcp3008 has 10 bit adc
it gives you number between 0 and 1023

'''

import spidev,time
spi=spidev.SpiDev()

spi.open(0, 0) #bus,service

def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4,0]) #xfer2(list of values[, speed_hz, delay_usec, bits_per_word])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out

while True:
    reading = analog_read(0)
    voltage = reading * 3.3 / 1024
    print("raeding= %d /t volatge =%f"%(reading,voltage))
    time.sleep(1)

