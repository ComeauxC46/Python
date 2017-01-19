########################################################################
#  Crosswalk.py                                                        #
#  Author: Chris Comeaux                                               #
#  Date: 1/11/2017                                                     #
#  Desciption: Simple program to control GPIO pins on rPI.             #
#              Stop Light cycles through green red yellow              #
#			   Press button to initiate walk sign                      #
#			   Based on the Tux Crossing project   					   # 
#			   found at https://projects.drogon.net/				   #
#			   raspberry-pi/gpio-examples/tux-crossing/                #
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
						      		     
#LED names
RED = 3  
YELLOW = 5
GREEN = 7
RED_WALK = 13
GREEN_WALK = 15

#Button
BUTTON = 11

'''
************************************************************************
''' 

'''
************************************************************************
						       DEFINITIONS                           '''
						       
def setUp():
	print("Initilizing...")
	#Set up pin layout (- BOARD = refer by pin number eg. 2 = pin 2)
	#					- BCM = refer by GPIO name eg. 2 = GPIO2 or pin 3)
	GPIO.setmode(GPIO.BOARD)

	#set pins as output
	for x in [3,5,7,13,15]:
		GPIO.setup(x, GPIO.OUT)
		if x == 7 or x == 13: #GREEN and RED_WALK ON
			GPIO.output(x, True) 
		else:
			GPIO.output(x, False)
			
	#detect pin 11 going from high to low
	GPIO.setup(BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	return
	
def waitForButton():
	print("Entering normal traffic cycle")
	while GPIO.input(11) == True:		#Button presses makes pin 11 go from high (true) to low (false)
		time.sleep(0.1)
	print("Walk request recieved")
	return

def stopLightRed():
	print("Stopping traffic")
	time.sleep(5)
	GPIO.output(GREEN, False)
	GPIO.output(YELLOW, True)
	time.sleep(2)
	GPIO.output(YELLOW, False)
	GPIO.output(RED, True) 
	time.sleep(1)
	return

def walkGreen():
	GPIO.output(RED_WALK, False)
	GPIO.output(GREEN_WALK, True)
	print("Walk")
	time.sleep(5)
	return
	
def timeWarning():
	print("Time is almost up..")
	GPIO.output(GREEN_WALK, False)
	GPIO.output(RED, False)
	
	for x in range(0,15):
		GPIO.output(YELLOW, True)
		GPIO.output(RED_WALK, True)
		time.sleep(0.2)
		GPIO.output(YELLOW, False)
		GPIO.output(RED_WALK, False)
		time.sleep(0.2)
		
	print("Time is up...")
	GPIO.output(GREEN, True)
	GPIO.output(RED_WALK, True)
	return
	
	

def exitHandler():
	GPIO.cleanup()
	return
							       
'''
************************************************************************
'''

'''
************************************************************************
						       MAIN                                  '''

def main():
	try:
		setUp()
		while True:
			waitForButton()
			stopLightRed()
			walkGreen()
			timeWarning()
			
			
	#Make sure the GPIO pins get cleaned up
	except KeyboardInterrupt:
		exitHandler()


'''
************************************************************************
''' 

if __name__ == '__main__':
	main()
	GPIO.cleanup()
	



