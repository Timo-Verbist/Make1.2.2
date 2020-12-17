#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "finished"

import random


def main():
    generator = random.randint(0, 9)
    guess = "guess"
    word = "word"
    while guess != word:
        words = ["cookie", "boat", "smartphone", "horse", "shoe", "drink", "fire", "picture", "game", "surf"]
        word = words[generator]
        guess = str(input("guess the word from the list.\n"))
        if guess == word:
            print("YOU GUESSED THE RIGHT WORD!!!")
            print("WELL DONE!!!")
        else:
            print("That's not the right word.\n Try again\n")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
