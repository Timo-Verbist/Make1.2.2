#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "finished"

# import


def main():
    while True:
        word = str(input("Give a word please.\n"))
        wordLength = len(word)
        print("uw woord achterstevoren is: ", end="")
        for i in range(wordLength, 0, -1):
                print(word[i-1], end="")

        print("\n\n")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
