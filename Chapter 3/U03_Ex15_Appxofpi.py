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
#
# import the math aprrox of pi, from directory
# get the imput of the aproxamation
#
import math
def main():
    pi = 0
    accuracy = 10
    for i in range(0, accuracy):
        pi += ((4.0 * (-1)**i) / (2*i + 1))
    print("The value of pi:" , math.pi)
    print("This is the approximation of pi:" , pi)
    difference = (math.pi - pi)
    print("This is the difference between the approximation of pi and the actual value of pi:" , difference)

main()
