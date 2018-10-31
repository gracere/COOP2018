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
    print("This program finds the sum of a cubed number.")
    n = int(input("Enter the number, that you would like the sum of that is cubed:"))
    i, sum = 1, 0
    while (i < n):
        if (i % 2 != 0):
            sum = sum + i * i
        i += 1
    print("Sum of all odd number is : ", sum)


main()
