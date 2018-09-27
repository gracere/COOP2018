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
#
# slope = ((y2 - y1) / (x2 - x1))
# find the users values
#
def main():
    variables = [0, 1, 2, 3]
    variables[0] = input("Please enter a your x1")
    variables[1] = input("Please enter a your x2")
    variables[2] = input("Please enter a your y1")
    variables[3] = input("Please enter a your y2")
    variables[0] = int(variables[0])
    variables[1] = int(variables[1])
    variables[2] = int(variables[2])
    variables[3] = int(variables[3])
    slope = ((variables[3] - variables[2]) / (variables[1] - variables[0]))
    print(slope)


main()
