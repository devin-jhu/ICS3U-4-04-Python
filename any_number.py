#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# The area and perimeter calculator

import random


def main():
    # this function is a guessing game

    counter = 1

    print("The number game")
    print("Guess a number between 1 and 9")

    # input
    random_number = random.randint(0, 9)
    guess_number_string = input("Enter your guess: ")

    # process & output
    while True:
        try:
            guess = int(guess_number_string)
            if guess == random_number:
                break
            elif guess > random_number:
                print("Guess lower")
            elif guess < random_number:
                print("Guess higher")
            else:
                print("What happened")

        except Exception:
            print("Not a number")

        guess_number_string = input("Try again: ")
        counter += 1

    # output
    print("You Win! It took {0} tries.".format(counter))
    print("\nDone.")


if __name__ == "__main__":
    main()
