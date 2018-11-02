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
# input that user number into sum = sum + number
# print out sum


def main():
    print("This program finds the sum of a number.")
    num = int(input("Enter a number: "))
    if num < 0:
        print("Enter a positive number")
    else:
        sum = 0
        while (num > 0):
            num * (num + 1) / 2
    print("The sum of first", num,  "natural numbers is:", sum)


main()


""" number = int(input("Enter a number, that you would like the sum of: "))
    sum1 = 0
    while number > 0:
        sum1 = sum1 + number
        number = number - 1
    print("The sum of first", number,  "natural numbers is:", sum1)"""