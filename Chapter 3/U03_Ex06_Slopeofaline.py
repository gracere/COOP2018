# U03_Ex06_Slopeofaline.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 6
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# This program finds the slope of line
#
# Algorithm (pseudocode)
# Print a program description
# find the users values for each variable( the variables are two sets of x and y points)
# insert into equation
# slope of a line = ((y2 - y1) / (x2 - x1))
# print the slope
#


def main():
    print("This program calculates the slope of a line with the x and y points:")
    x1 = input("Please enter a your x1: ")
    x2 = input("Please enter a your x2: ")
    y1 = input("Please enter a your y1: ")
    y2 = input("Please enter a your y2: ")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    slope = ((y2 - y1) / (x2 - x1))
    print("(", x1, ",", y1, ") , (", x2,  ",", y2, ")")
    print("The slope of your line is:", slope)


main()
