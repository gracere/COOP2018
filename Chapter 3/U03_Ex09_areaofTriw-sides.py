# U03_Ex09_areaofTriw-sides.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 28 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 9
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# Python Program to find the area of triangle
#
# Algorithm (pseudocode)
# Print program description
# find user numbers for all three sides
# input user numbers into equation: s = (a + b + c) / 2
# convert the sides into the area: area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print out input of area


def main():
    a = float(input('Enter first side: '))
    b = float(input('Enter second side: '))
    c = float(input('Enter third side: '))
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print('The area of the triangle is %0.2f:' %area)


main()
