#!/usr/bin/env python3

import random
from random import randint

LIMIT = 2 # fixed or constant variable

def display_title():
    print("Guess the number!")
    print()

def play_game():    
    number = random.randint(1, LIMIT) # generates a random number between 1 and 10
    print(f"I'm thinking of a number from 1 to {LIMIT}\n")
    count = 1

    while (guess := int(input("Your guess: "))) != number:
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        count += 1
    print(f"You guessed it in {count} ", end="")
    print("try." if count == 1 else "tries.")
     
def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        play_game()
        again = input("Would you like to play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

