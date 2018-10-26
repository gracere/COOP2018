# U03_Ex10_lenthofladder.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 30 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 10
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# This program finds the length of a ladder from the data of height, angle of ladder, and the radius
#
# Algorithm (pseudocode)
#
# find user variables: ex: need height,and the angle of the ladder in degrees.
# input into equation: radius = (pi/ 180) * angle of ladder, then length = height/ (sin(radius))
# print out input
#
import math


def main():
    print("This program calculates the length of a ladder.")
    height = eval(input("Please enter the height of the ladder "))
    deg = eval(input("Please enter the angle of the ladder in degrees "))
    rad = (math.pi/180) * deg
    length = height/(math.sin(rad))
    print("The length of the ladder must be ", length)


main()
