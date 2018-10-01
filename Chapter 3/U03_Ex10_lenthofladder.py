# U03_Ex10_lenthofladder.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 30 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise:
#    Source: Python Programming
#   Chapter:
#
# Program Description
#
# This finds the length of a ladder
#
# Algorithm (pseudocode)
#
# find user number
# input into equation
# print out input
#
import math
def main():


    height = eval(input("Please enter the height of the ladder "))
    deg = eval(input("Please enter the angle of the ladder in degrees "))
    rad = (math.pi/180) * deg
    length = height/(math.sin(rad))
    print("The length of the ladder must be ", length)


main()
