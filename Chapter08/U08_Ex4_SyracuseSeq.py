# U08_Ex4_SyracuseSeq.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 22 Mar 2019
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 4
#    Source: Python Programming
#   Chapter: 8
#
# Program Description
#
# This program with a user input puts a number through the syracuse cycle.
#
# Algorithm (pseudocode)
#
# Introduce program
#
# get user input
# if x is even, x = x/2
# or if x is odd, x = 3x + 1
# put user input through the loop until


def main():
    x = int(input("What is the integer starting value number that you want to use?: "))
    while Syracuse(x) == 1:
        print(x)


def Syracuse(x):
    even = (x + 2)
    if x == even:
        x = x / 2
        print(x)
        for x in range(x == 1):
            x = x / 2
            print(x)
    else:
        x = 3 * x + 1
        print(x)
        for x in range(x == 1):
            x = 3 * x + 1
            print(x)


if __name__ == '__main__':
    main()
