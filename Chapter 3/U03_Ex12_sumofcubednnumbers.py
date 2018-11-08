# U03_Ex12_sumofcubednnumbers.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 1 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 12
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# This program finds the sum of a cubed number.
#
# Algorithm (pseudocode)
# print the program description
# ask user for a number to find the sum of a number
# input that user number into first the sum of 0, then the sum + number, then number = number - 1
# print out sum


def main():
    print("This program sums the values of a number of cubes supplied by the user.")
    n = eval(input("How many positive integers' cubes would you like to add?"))
    total = 0
    for i in range(1, n+1):
        total = total + i**3

        print(total)


main()



