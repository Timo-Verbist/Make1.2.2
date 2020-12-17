#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

# import

lijst = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def main():
    for y in range(6):
        print("")
        for x in range(9):
            print(lijst[x][y], end="")

    print("\n\n en ook deze: ")

    for y in range(5, -1, -1):
        print("")
        for x in range(9):
            print(lijst[x][y], end="")

if __name__ == '__main__':  # code to execute if called from command-line
    main()
