# practice01.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 1 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 1
#    Source: Python Programming
#   Chapter: 3ish
#
# Program Description
#
# This program convert jules to Calories
#
# Algorithm (pseudocode)
# Introduce program
# loop until exit requested
#   get input: jules(0 to quit)
#   text for exit condition(break if true)
#   convert jules to calories (1 J = 0.239 cal)
#       calories = joules * 0.239
#   print result


def main():
    print("\nThis program converts Joules to Calories")
    while True:
        joules = float(input("\nEnter the amount of joules that you want to convert (zero to quit):"))
        if joules == 0:
            break
        calories = joules * 0.239
        print("\n", joules, "Joules is equivalent to", calories, "Calories")


main()
