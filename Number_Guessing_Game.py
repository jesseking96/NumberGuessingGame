# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint
playAgain = True
while playAgain:
    numberToGuess = randint(1,100)
    
    firstGuess = 0
    while firstGuess == 0:
        firstAttempt = int(input("Enter your first guess: "))
        if firstAttempt >= 1 and firstAttempt <= 100:
            firstGuess = firstAttempt
        else:
            print('OUT OF BOUNDS! TRY AGAIN!\n')
            
    firstDistance = abs(firstGuess - numberToGuess)
    if firstDistance <= 10:
        print('WARM!\n')
    else:
        print('COLD!\n')
    
    playerGuess = 0
    previousDistance = firstDistance
    guessCounter = 1
    while True:
        playerGuess = int(input('Enter your next guess: '))
        if playerGuess == numberToGuess:
            guessCounter += 1
            break;
        if playerGuess >=1 and playerGuess <= 100:
            currentDistance = abs(playerGuess - numberToGuess)
            if currentDistance < previousDistance:
                print('WARMER!\n')
            elif currentDistance > previousDistance:
                print('COLDER!\n')
            previousDistance = currentDistance
            guessCounter += 1
        else:
            print('OUT OF BOUNDS! TRY AGAIN!\n')
    while True:
        playAgainAnswer = input("YOU WIN! YOU WON IN {} GUESSES! WOULD YOU LIKE TO PLAY AGAIN? (Y/N)".format(guessCounter))
        if playAgainAnswer.upper() == 'Y':
            playAgain = True
            break
        elif playAgainAnswer.upper() == 'N':
            playAgain = False
            break
        else:
            print("INVALID INPUT. TRY AGAIN: ")
    
    

