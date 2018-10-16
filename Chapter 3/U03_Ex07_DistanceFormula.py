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


def main():
    x1 = input('Please enter a value for x1')
    x2 = input('Please enter a value for x2')
    y1 = input('Please enter a value for y1')
    y2 = input('Please enter a value for y2')
    print(x1, x2, y1, y2)
    xcords = x2 - x1
    print('Difference of X Co-Ordinates:', xcords)
    ycords = y2 - y1
    print('Difference of Y Co-Ordinates:', ycords)
    sumofx = xcords / 2
    sumofy = ycords / 2
    distform = sumofx + sumofy
    print("Distance of points:", distform)


main()
