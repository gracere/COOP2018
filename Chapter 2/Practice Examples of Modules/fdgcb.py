# fdgcb.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 21 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise:
#    Source: Python Programming
#   Chapter:
#
# Program Description
#
#
#
#
# Algorithm (pseudocode)
#
#
#
#
#
# factorial.py
# Program to compute the factorial of a number
# Illustrates for loop with an accumulator


def main():
    n = eval(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n, 1, -1):
    fact = fact * factor
    print("The factorial of", n, "is", fact)


main()
