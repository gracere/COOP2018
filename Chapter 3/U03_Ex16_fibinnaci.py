# U03_Ex16_fibinnaci.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 1 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 16
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# finds a number in the fibonacci sequence
#
# Algorithm (pseudocode)
# Print program description
# find user number
# input into equation
# print out input
#


def main():
    print("This is a program for the Fibonacci number for a value you input.")
    n = eval(input("Please insert the value of n:"))
    if n <= 0:
        print("Please insert positive integer")
    for i in range(n):
        if n == 1:
            print(1)
        if n > 1:
            equation = (n - 1) + (n - 2)
            print(equation)
            break


main()
