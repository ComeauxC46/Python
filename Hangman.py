########################################################################
#  Hangman.py                                                          #
#  Author: Chris Comeaux                                               #
#  Date: 1/6/2017                                                      #
#  Desciption: Simple hangman game written in Python 3 using Linux os. #
#              My first program written in Python.                     #
########################################################################

'''
************************************************************************
						       IMPORTS                               '''
from colorama import Fore, Style      	#Colored text and bold print
import os, random                     	#OS -> clear screen 
										#RANDOM -> random int
'''
************************************************************************
''' 

'''
************************************************************************
						       GLOBALS                               '''

HANGMAN = [ 							#Create list to hold the Hangman board
										#Some pictures adjusted for formatting reasons
'''
	*******
	|     |
	      |
	      |
	      |
	      |
	      |
	  ----------''',
'''
	*******
	|     |
	0     |
	      |
	      |
	      |
	      |
	  ----------''',
'''
	*******
	|     |
	0     |
	|     |
	      |
	      |
	      |
	  ----------''',
'''
	*******
	|     |
	0     |
       /|     |
	      |
	      |
	      |
	  ----------''',
'''
	*******
	|     |
	0     |
       /|\    |
	      |
	      |
	      |
	  ----------''',
'''
	*******
	|     |
	0     |
       /|\    |
       /      |
	      |
	      |
	  ----------''',
'''
	*******
	|     |
	0     |
       /|\    |
       / \    |
	      |
	      |
	  ----------'''
]	  
#Create Word List
words = '''acres adult advice arrangement attempt August Autumn border 
breeze brick calm canal Casey cast chose claws coach constantly contrast 
cookies customs damage Danny deeply depth discussion doll donkey Egypt 
Ellen essential exchange exist explanation facing film finest fireplace 
floating folks fort garage grabbed grandmother habit happily Harry heading 
hunter Illinois image independent instant January kids label Lee lungs 
manufacturing Martin mathematics melted memory mill mission monkey Mount 
mysterious neighborhood Norway nuts occasionally official ourselves palace 
Pennsylvania Philadelphia plates poetry policeman positive possibly practical 
pride promised recall relationship remarkable require rhyme rocky rubbed 
rush sale satellites satisfied scared selection shake shaking shallow 
shout silly simplest slight slip slope soap solar species spin stiff 
swung tales thumb tobacco toy trap treated tune University vapor vessels 
wealth wolf zoo'''.split()
#Found on: http://www.manythings.org/vocabulary/lists/l/words.php?f=noll15

'''
************************************************************************
''' 

'''
************************************************************************
						   GAME FUNCTIONS                            '''

def startGame():				#Stars the game
	drawGameBoard()
	getUserInput()
	return
	
def getWord():					#Generates random word from word list
	return words[random.randint(0,len(words)-1)]
	
def drawGameBoard():			#Print the Game Board
	print("\tH A N G M A N\n")
	print ("Missed letters = %s" %missedLetters)
	print(HANGMAN[len(missedLetters)])
	blanks()
	return
	
def getUserInput():				#Get user input and check it
	while True:
		userIn = input("\nGuess: ")
		
		if userIn.lower() not in 'abcdefghijklmnopqrstuvwxyz':
			print("Please enter a letter.")
		
		elif userIn in guessedLetters:
			print("You have already guessed that letter.")
		
		elif len(userIn) != 1:
			print("Only enter 1 character")
		
		else:
			break
			
	processInput(userIn.lower())
	return
																
def find(s, ch):				#Search a string (s) for a character (ch), returns list of positions where ch occures in s
	return [i for i, ltr in enumerate(s.lower()) if ltr == ch]
	
def processInput(userIn):		#Process user input and update game board
	global missedLetters
	global guesses
	global guessedLetters
	
	guessedLetters = guessedLetters + userIn
	guesses = guesses + 1
	
	if userIn in currentWord.lower():
		blanks(find(currentWord.lower(), userIn))
		if blank == currentWord.lower():
			os.system("clear") 	#clear game board
			drawGameBoard()    	#update the game board
			gameOver(True)
		return

	else:
		missedLetters = missedLetters + userIn
		if len(missedLetters) == len(HANGMAN)-1:
			os.system("clear")  #clear game board
			drawGameBoard()     #update the game board
			gameOver(False)
		return
		
def blanks(pos=None):			#Updates and prints blanks on game board
	global blank
	if pos == None: 			#If no position passed in then just print blanks again
		print("\t" + blank)
	else:
		for x in pos:
			blank = blank[:x] + currentWord[x] + blank[x+1:]
		print("\t" + blank)

def gameOver(won):				#Prints prompt when the game has ended
	if won:
		print ("Congratulations! It only took you " + str(guesses) + " guesses to win the game.")
		playAgain()
		return
	else:
		print("\tG A M E O V E R...\nYou took too many guesses...")
		print("The the word was ", end='')
		print(Style.BRIGHT, end='')
		print (Fore.RED + currentWord)
		print(Style.RESET_ALL, end='')
		playAgain()
		return
		
def playAgain():				#Prompts user and resets game or closes program
	global gameDone
	global currentWord
	global wordlen
	global missedLetters
	global guessedLetters
	global guesses
	global blank

	answ = input("Would you like to play again? (y,n): ")
	if answ.lower() == 'y': 	#reset the game variables and clear the screen
		currentWord = getWord()
		wordlen= len(currentWord)
		missedLetters = ""
		guessedLetters = ""
		guesses = 0
		blank = "~" * wordlen
		gameDone = False
		os.system("clear")
		return
	else:
		gameDone = True
		return
'''
************************************************************************
''' 
		 
'''
************************************************************************
						 Game Set-Up and Loop                        '''

#Primary game set up (Global variables)
currentWord = getWord()
wordlen= len(currentWord)
guessedLetters = ""
missedLetters = ""
guesses = 0
blank = "~" * wordlen
gameDone = False

#Start the game
while not gameDone:
	startGame()
	os.system("clear") #clear the screen 
	
os.system("exit")
'''
************************************************************************
'''


	

