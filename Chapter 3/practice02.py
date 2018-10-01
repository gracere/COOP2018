# practice02.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 1 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 2
#    Source: Python Programming
#   Chapter: 3ish
#
# Program Description
#
# This program is an interactive calculator that accepts mathematical expressions
#
# Algorithm (pseudocode)
#   Introduce program
#   Loop until exit requested
#       Get input(mathematical expression: (0 to quit))
#       Test for exit
#       Evaluate mathematical expression
#       Print result
#


def main():
    print("This program is an interactive calculator that accepts mathematical expressions.")
    while True:
        me = input("Please enter a mathematical expression to evaluate (0 to quit): ")
        if me == "0":
            break
        result = eval(me)
        print("The expression", me, "is equivilent to", result)


main()
