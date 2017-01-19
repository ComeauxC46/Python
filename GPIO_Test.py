########################################################################
#  GPIO_Test.py                                                        #
#  Author: Chris Comeaux                                               #
#  Date: 1/11/2017                                                     #
#  Desciption: Simple program to control GPIO pins on rPI.             #
#              Controls a single LED light connected to GPIO 2         #
######################################################################## 


'''
************************************************************************
						       IMPORTS                               '''
import RPi.GPIO as GPIO
import time

'''
************************************************************************
''' 

'''
************************************************************************
						       FUNCTION                              '''
						     
LONG = 1
SHORT = .5

#Set up pin layout (- BOARD = refer by pin number eg. 2 = pin 2)
#					- BCM = refer by GPIO name eg. 2 = GPIO2 or pin 3)
GPIO.setmode(GPIO.BOARD)

#set pin as output
GPIO.setup(3, GPIO.OUT)

#Loop to make light blink
for x in range(0,4):
	GPIO.output(3,True)
	time.sleep(LONG)
	GPIO.output(3,False)
	time.sleep(SHORT)

	

GPIO.cleanup()

'''
************************************************************************
''' 
