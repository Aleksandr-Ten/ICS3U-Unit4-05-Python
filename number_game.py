#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: April 2022
# This program tells if the number user inputs is correct

import random


def main():
    # this function is the game

    # input, process & output
    random_number = random.randint(0, 9)  # a number between 0-9
    while True:
        try:
            number_guessed_as_string = input("Guess a number between 0 and 9: ")
            number_guessed = int(number_guessed_as_string)
            if number_guessed == random_number:
                print("\nYou guessed correctly!")
                break
            else:
                if number_guessed > random_number:
                    print("That number is too high, guess lower.")
                else:
                    print("That number is too low, guess higher.")
        except Exception:
            print("Invalid input. Please try again.")

    print("\nDone")


if __name__ == "__main__":
    main()
