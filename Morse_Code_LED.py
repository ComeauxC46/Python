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
						       
#Length of blink
LONG = 0.75 # '-' or dah
SHORT = 0.25 # '.' or di/dit
						      
#Morse Code based on International Standard
#https://en.wikipedia.org/wiki/American_Morse_code
MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
			  'D': '-..',    'E': '.',      'F': '..-.',
			  'G': '--.',    'H': '....',   'I': '..',
			  'J': '.---',   'K': '-.-',    'L': '.-..',
			  'M': '--',     'N': '-.',     'O': '---',
			  'P': '.--.',   'Q': '--.-',   'R': '.-.',
			  'S': '...',    'T': '-',      'U': '..-',
			  'V': '...-',   'W': '.--',    'X': '-..-',
			  'Y': '-.--',   'Z': '--..',	' ': '',
			  
			  '0': '-----',  '1': '.----',  '2': '..---',
			  '3': '...--',  '4': '....-',  '5': '.....',
			  '6': '-....',  '7': '--...',  '8': '---..',
			  '9': '----.' 
			 }

#Converts '.'(dit) and '-'(dah) into time units
CONVERTER =  {'.': SHORT, '-': LONG}
		     
#LED names  
MORSE_PIN = 5
SPACE_PIN = 3

'''
************************************************************************
''' 

'''
************************************************************************
						       DEFINITIONS                           '''
						       
def setUp():
	#Set up pin layout (- BOARD = refer by pin number eg. 2 = pin 2)
	#					- BCM = refer by GPIO name eg. 2 = GPIO2 or pin 3)
	GPIO.setmode(GPIO.BOARD)

	#set pin as output and turn off
	GPIO.setup(SPACE_PIN, GPIO.OUT)
	GPIO.setup(MORSE_PIN, GPIO.OUT)
	GPIO.output(SPACE_PIN, False)
	GPIO.output(MORSE_PIN, False)	
	return
		       
def convertToMorse(message):
	#convert message into Morse Code
	code = [] #This will hold the converted message

	for char in message:
		#If the char is not in coverstion, skip it
		if char.lower() not in 'abcdefghijklmnopqrstuvwxyz0123456789 ':
			continue
		code.append(MORSE_CODE[char.upper()])
	return code

def convertToLED(code):
	#Convert code to LED Blinks
	for x in range(0, len(code)):
		if code[x] == '': 					#indicate space between word with blink of space led
			GPIO.output(SPACE_PIN,True)
			time.sleep(SHORT)
			GPIO.output(SPACE_PIN,False)
			time.sleep(SHORT)
			continue
		time.sleep(SHORT)					#Time between letters		
		for y in range(0, len(code[x])):
			GPIO.output(MORSE_PIN,True)
			time.sleep(CONVERTER[code[x][y]])
			GPIO.output(MORSE_PIN,False)
			time.sleep(SHORT)			
	

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
	setUp()
	#Get message from user
	message = input("Please input your message: ")
	#Convert message to code then to LED Blinks
	convertToLED(convertToMorse(message))
	return


'''
************************************************************************
''' 

if __name__ == '__main__':
	main()
	
#Make sure the GPIO pins get cleaned up
atexit.register(exitHandler)
