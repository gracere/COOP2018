# U03_Ex11_sumof1nnumber.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 1 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 11
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# This program finds the sum of a number
#
# Algorithm (pseudocode)
# print the program description
# ask user for a number to find the sum of a number
# input that user number into first the sum of 0, then the sum + number, then number = number - 1
# print out sum


def main():
    print("This program finds the sum of a number.")
    number = int(input("Enter a number, that you would like the sum of: "))
    sum1 = 0
    while number > 0:
        sum1 = sum1+number
        number = number-1
    print("The sum of first", number,  "natural numbers is:", sum1)


main()
