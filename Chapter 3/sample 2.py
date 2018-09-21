# sample 2.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 21 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise:
#    Source: Python Programming
#   Chapter:
#
# Program Description
#
#
#
#
# Algorithm (pseudocode)
#
#
#
#
#
# quadratic.py
# A program that computes the real roots of a quadratic equation.
# Illustrates use of the math library.
# Note: This program crashes if the equation has no real roots.
import math # Makes the math library available.
def main():
 print("This program finds the real solutions to a quadratic")
 print()
 a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
 discRoot = math.sqrt(b * b - 4 * a * c)
 root1 = (-b + discRoot) / (2 * a)
 root2 = (-b - discRoot) / (2 * a)
 print()
 print("The solutions are:", root1, root2 )