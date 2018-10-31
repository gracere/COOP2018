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


def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(9))


def main():
    print("This program finds the nth number in the Fibonacci Sequence.")
    n = input("Please type a number that you would wish to find:")
    Fibonacci(n)
    print(Fibonacci(n))


main()
