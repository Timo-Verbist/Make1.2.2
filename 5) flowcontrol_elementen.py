#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

# import


def main():
    number = ""
    while number != 0:
        number = int(input("\ngive a number and we'll print somthing out. ('0' to quit)\n"))
        if number < 3:
            print("that's a very small number")
        elif 3 < number < 100:
            print("that's a medioker number")
        else:
            print("That's a very big number!")
        for i in range(number):
            print("your number is: " + str(number))



if __name__ == '__main__':  # code to execute if called from command-line
    main()
