########################################################################
#  Morse_Code_LED.py                                                   #
#  Author: Chris Comeaux                                               #
#  Date: 1/11/2017                                                     #
#  Desciption: Simple program to control GPIO pins on rPI.             #
#              Converts message into Morse Code by illuminating        #
#			   LED connected to Pin 5. LED connected to Pin 3          #
#			   used to indicate space between words					   #
######################################################################## 


'''
************************************************************************
						       IMPORTS                               '''
import RPi.GPIO as GPIO
import time, atexit

'''
************************************************************************
''' 

'''
************************************************************************
						       CONSTANTS                             '''
						       

'''
************************************************************************
''' 

'''
************************************************************************
						       DEFINITIONS                           '''
						       

def exitHandler():
	GPIO.cleanup()
	return
							       
'''
************************************************************************
'''

'''
************************************************************************
						       MAIN                                  '''



#Set up pin layout (- BOARD = refer by pin number eg. 2 = pin 2)
#					- BCM = refer by GPIO name eg. 2 = GPIO2 or pin 3)
GPIO.setmode(GPIO.BOARD)

#set pin as output and turn off
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.output(3, False)
GPIO.output(5, False)
GPIO.output(7, False)	
		   
	
while True:
	GPIO.output(3, True)
	time.sleep(3)
	GPIO.output(3, False)
	GPIO.output(5, True)
	time.sleep(2)
	GPIO.output(5, False)
	GPIO.output(7, True)
	time.sleep(3)
	GPIO.output(7, False)



'''
************************************************************************
''' 


#Make sure the GPIO pins get cleaned up
atexit.register(exitHandler)
