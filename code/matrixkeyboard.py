'''
simple button input
array for loop
 1 2 3 A
 4 5 6 B
 7 8 9 C
 * 0 # D

 4 rows
 4 columns
 approach
 8 pin as GPIO pins
 setup column as output  and set low
 set up row pins as inputs with pull up resistor
 inputs are set high
  when a button is pressed input becomes low
  indicating which button has been pressed

'''
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
matrix=[[1,2,3,'A'],[4,5,6,'B'],[7,8,9,'C'],['*',0,'#','D']]
ROW=[7,11,13,15]
COL=[12,16,18,22]
for j in range(4):
    GPIO.setup(COL[j],GPIO.OUT)
    GPIO.output(COL[j],1)
for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    while(True):
        for j in range(4):
            GPIO.output(COL[j],0)
            for i in range(4):
                if GPIO.input(ROW[i]) ==0:
                    print matrix[i][j]
                    while(GPIO.input(ROW[i])==0):
                        pass
            GPIO.output(COL[j],i)


except KeyboardInterrupt:
    GPIO.cleanup()


