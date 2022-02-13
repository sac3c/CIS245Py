# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Steve Colletta>
# Creation Date: <Feb 13, 2022>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('You are in a land full of dragons. In front of you, ')
	print('you see two caves. In one cave, the dragon is friendly')
	print('and will share his treasure with you. The other dragon')
	print('is greedy and hungry, and will eat you on sight.')
	#too many quotation marks, added separate print statements so text wasn't skewed when displayed
	print()

def chooseCave():
		cave = ''  #spaces used not indentation
		while cave != '1' and cave != '2':  #not sure why "not equal" used instead of True to give option to user to quit, and indentation issue
				print('Which cave will you go into? (1 or 2)') #indentation issue
				cave = input()	#indentation issue

		return cave   #"cave" not caves, indentation issue

def checkCave(chosenCave):
	print('You approach the cave...')
	time.sleep(2)  #comment line moved next to command
	print('It is dark and spooky...')
	time.sleep(3)  #comment incorrectly identified as 2 while sleep set for 3
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	time.sleep(2)   #sleep for 2 seconds
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print ('Gobbles you down in one bite!') #missing parenthesis

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y': #missing double "=="
	displayIntro()
	caveNumber = chooseCave() #chooseCave not choosecave
	checkCave(caveNumber)

	print('Do you want to play again? (yes or no)')
	playAgain = input()
	#if playAgain == "no": don't need if statement while in a loop already
	print("Thanks for planing") #indentation


