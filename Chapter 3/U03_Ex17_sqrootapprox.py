# U03_Ex17_sqrootapprox.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 1 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 17
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# Find the approximation of a square root, using Newtons square root method.
#
# Algorithm (pseudocode)
# import math
# print introduction
# get input of number
# get input of number of tries
# store actual sqrt as variable
# divide input of number by 2 and store as variable
# for loop making it loop the number of tries
# make the estimation grow by making it a variable of itself (guess = (guess + (number/guess))/2)
# subtract exact answer from the estimated one to find the deviation
# print conclusion
import math


def main():
    print("This program uses Newtons method to compute square roots.")

    number = float(input("What is the number you wish to find the square root of?"))
    tries = int(input("How many times would you like to use the formula to get closer?"))
    answer = math.sqrt(number)
    guess = number/2

    for i in range(tries):
        guess = (guess + (number/guess))/2
        deviation = float(answer - guess)

    print(" ")
    print("The approximation of the square root of", number, "is", str(round(guess, 4)) + ", which")
    print("is exactly", deviation, "from the actual square root of,", answer,)


main()
