# U03_Ex15_Appxofpi.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 15
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# This program computes the approximation of pi
#
# Algorithm (pseudocode)
# import math
# Print a program description
# get accuracy input from user
# insert into pi equation(pi += ((4.0 * (-1)**i) / (2*i + 1)))
# print the value of pi
# print the approximation of pi
# put value of pi and approximation of pi into difference equation
# print the difference
#
import math


def main():
    print("This program approximations pi, and then calculates the difference from that and the actual value of pi.")
    pi = 0
    accuracy = int("What is the accuracy of the approximation of pi?")
    for i in range(0, accuracy):
        pi += ((4.0 * (-1)**i) / (2*i + 1))
    print("The value of pi:", math.pi)
    print("This is the approximation of pi:", pi)
    difference = (math.pi - pi)
    print("This is the difference between the approximation of pi and the actual value of pi:", difference)


main()
