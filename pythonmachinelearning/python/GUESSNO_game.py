#the perfect guess game 
#write a program that generates a random number between 1 and 1000 and asks the user to guess it
#if the guess is too high, the program should print "Too high, try again"
#if the guess is too low, the program should print "Too low, try again"
#when the user guesses the number , the program displays the total number of guesses 

import random
N=random.randint(1, 1000)
guess=0
count=0
guess=input("guess a number between 1 and 1000 : ")
try:
    guess==int(guess)
    guess=int(guess)
    while guess!=N:
        if guess < N:
            print("low, try again")
        else:
            print("high, try again")
        guess=input("guess a number between 1 and 1000 : ")
        guess=int(guess)
        count+=1
        continue
    print("you guessed it in", count, "tries")
except ValueError:
    print("Please enter a valid integer.")


        

    