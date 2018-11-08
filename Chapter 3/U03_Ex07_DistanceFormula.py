# U03_Ex07_DistanceFormula.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 7
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# This program calculates the distance formula
#
# Algorithm (pseudocode)
# Print program description
# Get data points from user
# separate data and find parts of data, then put together
# use formula to do that: (x1 + x2 / 2) + (y1 + y2 / 2))
# insert distance formula into code
# print findings

import math


def main():
    print("This program computes the distance formula of two sets of points.")
    x1 = input('Please enter a value for x1: ')
    x2 = input('Please enter a value for x2: ')
    y1 = input('Please enter a value for y1: ')
    y2 = input('Please enter a value for y2: ')
    d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    print(" ")
    print("The distance between points (" + str(x1) + ",", str(y1) + ") and ("
          + str(x2) + ",", str(y2) + ") is", round(d, 2))


main()
